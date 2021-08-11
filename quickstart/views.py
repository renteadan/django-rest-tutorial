from quickstart.models import ShopItem
from rest_framework import generics
from quickstart.serializers import ShopItemSerializer


class ShopItemListView(generics.ListCreateAPIView):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer


class ShopItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
