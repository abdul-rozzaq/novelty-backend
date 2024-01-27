from django.urls import path

from .views import (
    get_carousel_items, 
    get_genres, 
    get_locations,
    shop_login,
    shop_register,
)


urlpatterns = [
    path('carousel-items/', get_carousel_items),
    path('genres/', get_genres),
    path('locations/', get_locations),

    path('login/', shop_login),
    path('register/', shop_register),
]
