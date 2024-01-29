from django.contrib import admin
from .models import Genre, CarouselItem, Book


class BookAdmin(admin.ModelAdmin):
    list_display = [
        x.name for x in Book._meta.fields if x.name not in ['description']]
    list_filter = ['shop', 'genres__name']


admin.site.register(Genre)
admin.site.register(CarouselItem)
admin.site.register(Book, BookAdmin)
