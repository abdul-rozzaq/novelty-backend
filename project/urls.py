from django.urls import path


from .views import *

urlpatterns = [
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    
    path('', home_page, name='home_page'),
    path('books/', books_page, name='books_page'),
    path('orders/', orders_page, name='orders_page'),
    path('comments/', comments_page, name='comments_page'),
    path('collections/', collections_page, name='collections_page'),
    path('chat/', chat_page, name='chat_page'),
    path('logout/', logout, name='logout'),
    
    path('edit-book/<uuid:pk>/', edit_book, name='edit_book_page'),

    path('get-book-image/<uuid:image_id>/<str:size>/', get_image, name='book_image_resize'),
]
