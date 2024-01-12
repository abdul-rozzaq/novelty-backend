from django.urls import path

from .views import get_carousel_items


urlpatterns = [
    path('carousel-items/', get_carousel_items),
]