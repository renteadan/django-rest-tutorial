from quickstart.models import Item, ShoppingListItem, ShoppingList
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'price', 'name', 'description']


class ShoppingListItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'quantity', 'item']


class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(many=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'name', 'items']
