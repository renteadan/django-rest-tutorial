from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, through='ShoppingListItem')

    def __str__(self):
        return self.name


class ShoppingListItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.name + ' (' + str(self.quantity) + ')'
