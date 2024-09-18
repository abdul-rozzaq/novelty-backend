from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Book, BookImage

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        print(args)
        print(len(args))
        
        
        # if args:
        #     files = args[1]
        #     self.images = files.getlist('images')[:6]

    class Meta:
        model = Book
        fields = ['shop', 'name', 'description', 'price', 'author', 'genres', 'count']

    def save(self, commit=True):
        book = super().save(commit)
        
        for img in self.images:
            BookImage.objects.create(
                book=book,
                image=img
            )
        return book 
    
    
class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'price', 'author', 'genres', 'count']