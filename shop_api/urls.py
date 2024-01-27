from django.urls import path

from .views import (
    shop_login,
    shop_register,
    test,
)


urlpatterns = [
    path('login/', shop_login),
    path('register/', shop_register),
    path('test/', test),
]
