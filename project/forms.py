from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Book, BookImage


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.images = kwargs["files"].getlist("images")[:6]

    class Meta:
        model = Book
        fields = [
            "shop",
            "name",
            "description",
            "price",
            "author",
            "genres",
            "count",
            "isbn",
        ]

    def save(self, commit=True):
        book = super().save(commit)

        for img in self.images:
            BookImage.objects.create(book=book, image=img)

        return book


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "description", "price", "author", "genres", "count"]

    def save(self, commit=True):

        if self.files:

            self.instance.images.all().delete()

            for img in self.files.getlist("images")[:6]:
                BookImage.objects.create(book=self.instance, image=img)

        return super().save(commit)
