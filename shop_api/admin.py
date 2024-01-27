from django.contrib import admin
from .models import Shop, Token


class ShopAdmin(admin.ModelAdmin):

    list_display = ['name', 'login', 'image']


admin.site.register(Token)
admin.site.register(Shop, ShopAdmin)
