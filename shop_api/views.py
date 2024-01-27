from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.response import Response

from .serializers import ShopSerializer, TokenSerializer
from .models import Shop, Token
from .auth import TokenAuthentication

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
@authentication_classes([TokenAuthentication])
def test(request):
    
    print(request.shop)
    return Response(status=status.HTTP_200_OK)