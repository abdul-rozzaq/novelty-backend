from django.urls import path

from .views import (
    get_carousel_items,
    get_genres,
    get_books,
)


urlpatterns = [
    path('carousel-items/', get_carousel_items),
    path('genres/', get_genres),
    path('get-books/', get_books),
]
