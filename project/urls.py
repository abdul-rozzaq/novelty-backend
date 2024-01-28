from django.urls import path


from .views import get_image

urlpatterns = [
    path('get-book-image/<str:book_id>/<str:size>/',
         get_image, name='book_image_resize'),

]
