from django.urls import path


from .views import (
    get_image, 
    home_page, 
    login_page, 
    register_page,
    logout
)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout, name='logout'),

    path('get-book-image/<str:book_id>/<str:size>/',
         get_image, name='book_image_resize'),
]
