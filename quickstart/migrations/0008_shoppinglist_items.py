# Generated by Django 3.2.6 on 2021-08-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_auto_20210813_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='items',
            field=models.ManyToManyField(through='quickstart.ShopItem', to='quickstart.Item'),
        ),
    ]
