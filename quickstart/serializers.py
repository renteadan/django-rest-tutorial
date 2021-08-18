from quickstart.models import Item, ShoppingListItem, ShoppingList
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Item
        fields = ['id', 'price', 'name', 'description']


class ShoppingListItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ShoppingListItem
        fields = ['id', 'quantity', 'item']


class ShoppingListSerializer(serializers.ModelSerializer):
    items = ShoppingListItemSerializer(
        source='shoppinglistitem_set', many=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'name', 'items']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.items.set([])
        instance.save()
        items = validated_data.get('shoppinglistitem_set')
        for item in items:
            item_id = item.get('id')
            print(item_id)
            if item_id:
                item_obj = ShoppingListItem.objects.get(id=item_id)
                item_obj.quantity = item.get('quantity')
                item_obj.save()
            else:
                base_item_id = item.get('item').get('id')
                if base_item_id:
                    base_item = Item.objects.get(id=base_item_id)
                    ShoppingListItem.objects.create(
                        list=instance,
                        item=base_item,
                        quantity=item.get('quantity')
                    )
                else:
                    raise serializers.ValidationError(
                        'Item id is required.')
        return instance
