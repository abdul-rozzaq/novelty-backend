from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .serializers import ShopSerializer, TokenSerializer
from .models import Shop, Token, Region
from .auth import TokenAuthentication

from accounts import auth, permissions

from PIL import Image
from io import BytesIO


def get_image(request, shop_id, size):
    
    size = float(size) 
    shop = Shop.objects.get(id=shop_id)
    

    original_image = Image.open(shop.image.path)
    resized_image = original_image.resize((int(shop.image.width * float(size)), int(shop.image.height * float(size))))

    buffer = BytesIO()
    resized_image.save(buffer, format="png")
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename=f'{shop.image.name.split(".")[0]}.png')


@api_view(['GET'])
@authentication_classes([auth.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_locations(request):
    return Response([{'id': x.id, 'name': x.name, 'districts': [{'id': y.id, 'name': y.name} for y in x.districts.all()]} for x in Region.objects.all()])


@api_view(['POST'])
def shop_register(request):
    data = request.data

    serializer = ShopSerializer(data=data, context={'request': request})

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def shop_login(request):
    login = request.data.get('login')
    password = request.data.get('password')

    shop = Shop.authenticate(login, password)

    if shop:
        token, created = Token.objects.get_or_create(shop=shop)
        shop_serializer = ShopSerializer(shop)
        token_serializer = TokenSerializer(token)

        return Response({'shop': shop_serializer.data, 'token': token_serializer.data})
    else:
        return Response({'error': 'Invalid login or password'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
def test(request):

    shop: Shop = Shop.objects.get(id='7403bb4a-b9b7-4545-935e-0953341e6ec9')

    serializer = ShopSerializer(shop, context={'request': request})

    return Response(serializer.data, status=status.HTTP_200_OK)
