
from rest_framework import serializers

from project.models import Book
from django.urls import reverse


class BookSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_image(self, shop):
        request = self.context.get('request')

        return [
            request.build_absolute_uri(reverse('book_image_resize', kwargs={'book_id': shop.id, 'size': x})) for x in [1, 0.7, 0.5, 0.3]
        ]

    def get_genres(self, book):
        return [{'id': x.id, 'name': x.name} for x in book.genres.all()]
