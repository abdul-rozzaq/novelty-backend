from rest_framework import serializers
from .models import Shop, Token
from django.urls import reverse


class ShopSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = '__all__'

    def get_image(self, shop):
        request = self.context.get('request')

        return [
            request.build_absolute_uri(reverse('shop_image_resize', kwargs={'shop_id': shop.id, 'size': x})) for x in [1, 0.7, 0.5, 0.3]
        ]


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'shop', 'created')
