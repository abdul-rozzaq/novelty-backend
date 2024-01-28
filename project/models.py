import uuid
from django.db import models

from shop_api.models import Shop


class Genre(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class CarouselItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='carousel-images/')

    def __str__(self) -> str:
        return str(self.id)


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
