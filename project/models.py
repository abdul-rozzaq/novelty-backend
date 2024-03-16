import uuid
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class CarouselItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='carousel-images/')

    def __str__(self) -> str:
        return str(self.id)


from django.db import models
import binascii
import os

import uuid


class Region(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class District(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='shops-image/',
                              default='images/default-shop-image.jpg')
    name = models.CharField(max_length=256)
    login = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def authenticate(login, password):
        try:
            return Shop.objects.get(login=login, password=password)
        except Shop.DoesNotExist:
            return None


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book-images/')
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    
    author = models.CharField(max_length=256)
    
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return self.name
