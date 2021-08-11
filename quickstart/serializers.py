from quickstart.models import ShopItem
from rest_framework import serializers


class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItem
        fields = ['price', 'name', 'description']
