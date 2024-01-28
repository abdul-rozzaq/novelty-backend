from django.urls import path

from .views import (
    shop_login,
    shop_register,
    get_locations,
    get_image,
    test,
)


urlpatterns = [
    path('login/', shop_login),
    path('get-image/<str:shop_id>/<str:size>/', get_image, name='shop_image_resize'),
    path('register/', shop_register),
    path('locations/', get_locations),
    path('test/', test),
]
