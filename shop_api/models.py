from django.db import models
import binascii
import os

import uuid


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


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    shop = models.ForeignKey(
        Shop, related_name='tokens', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(30)).decode()

    def __str__(self):
        return self.key
