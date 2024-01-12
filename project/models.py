import uuid
from django.db import models


class Genre(models.Model):
    image = models.ImageField(upload_to='genre-icons/')
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class CarouselItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='carousel-images/')

    def __str__(self) -> str:
        return str(self.id)
