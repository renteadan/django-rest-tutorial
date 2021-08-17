from quickstart.models import Item, ShoppingList
from rest_framework import viewsets
from quickstart.serializers import ItemSerializer, ShoppingListSerializer


class ItemListView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ShoppingListView(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
