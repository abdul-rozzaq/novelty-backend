from django.db import models
from django.utils.translation import gettext_lazy as _
import os
import binascii
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=13, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __int__(self) -> int:
        return self.pk

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    @staticmethod
    def authenticate(phone):
        try:
            return User.objects.get(phone=phone)
        except User.DoesNotExist:
            return None

    def full_name(self):
        return self.first_name + ' ' + self.last_name

class Token(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User, related_name='auth_token', on_delete=models.CASCADE, verbose_name=_("User"))
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(30)).decode()

    def __str__(self):
        return self.key
