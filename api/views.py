from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from accounts.permissions import IsAuthenticated
from accounts.auth import TokenAuthentication
from api.serializers import ShopSerializer, TokenSerializer
from project.models import CarouselItem, Genre, Region, Shop, Token


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_carousel_items(request):
    return Response([x.image.url for x in CarouselItem.objects.all()])


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_genres(request):
    return Response([{'id': x.id, 'name': x.name} for x in Genre.objects.all()])


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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
