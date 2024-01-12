from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from .models import Token, User
from .serializers import UserSerializer, TokenSerializer


class LoginView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        user = User.authenticate(phone=phone)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            token_serializer = TokenSerializer(token)
            
            return Response({'user': user_serializer.data, 'token': token_serializer.data})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out'})


class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            user_serializer = UserSerializer(user)
            token_serializer = TokenSerializer(token)
            
            return Response({'user': user_serializer.data, 'token': token_serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
