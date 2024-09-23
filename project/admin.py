from django.contrib import admin
from .models import (
    Genre,
    CarouselItem,
    Book,
    Shop,
    District,
    Region,
    BookImage,
    BookReview,
)


class BookAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Book._meta.fields if x.name not in ["description"]]
    list_filter = ["shop", "genres__name"]
    search_fields = ["name"]


class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "login", "image"]


class BookImageAdmin(admin.ModelAdmin):
    list_filter = ["book", "book__name"]


admin.site.register(Shop, ShopAdmin)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(BookReview)
admin.site.register(BookImage, BookImageAdmin)

admin.site.register(Genre)
admin.site.register(CarouselItem)
admin.site.register(Book, BookAdmin)
