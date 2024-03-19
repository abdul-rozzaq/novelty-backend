import base64

from django.urls import reverse
from django.core.files.base import ContentFile

from rest_framework import serializers

from project.models import Book


class BookSerializer(serializers.ModelSerializer):
    shop = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def get_image(self, book):
        request = self.context.get('request')

        return [
            [
                request.build_absolute_uri(reverse('book_image_resize', kwargs={'image_id': img.id, 'size': x})) for x in [1, 0.7, 0.5, 0.3]
            ] for img in book.images.all()
        ]

    def get_genres(self, book):
        return [{'id': x.id, 'name': x.name} for x in book.genres.all()]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['images'] = self.get_image(instance)
        data['genres'] = self.get_genres(instance)

        return data

    def create(self, validated_data):
        validated_data['shop'] = self.context['request'].shop
        return super().create(validated_data)

    def validate_empty_values(self, data):

        data = {**data}

        if isinstance(data['image'], str):
            name, imagestr = data['image'].split(';')

            data['image'] = ContentFile(base64.b64decode(imagestr), name=name)

        
        print(data)
        return super().validate_empty_values(data)
