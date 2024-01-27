from django.contrib import admin
from .models import Genre, CarouselItem, Region, Shop



class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'login', 'image']





admin.site.register(Genre)
admin.site.register(CarouselItem)
admin.site.register(Region)
admin.site.register(Shop, ShopAdmin)
