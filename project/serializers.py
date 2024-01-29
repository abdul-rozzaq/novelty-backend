
from rest_framework import serializers

from project.models import Book
from django.urls import reverse


class BookSerializer(serializers.ModelSerializer):
    shop = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def get_image(self, book):
        request = self.context.get('request')

        return [
            request.build_absolute_uri(reverse('book_image_resize', kwargs={'book_id': book.id, 'size': x})) for x in [1, 0.7, 0.5, 0.3]
        ]

    def get_genres(self, book):
        return [{'id': x.id, 'name': x.name} for x in book.genres.all()]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['shop'] = self.get_image(instance)
        data['genres'] = self.get_genres(instance)

        return data

    def create(self, validated_data):
        validated_data['shop'] = self.context['request'].shop
        return super().create(validated_data)
