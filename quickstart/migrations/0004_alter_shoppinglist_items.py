# Generated by Django 3.2.6 on 2021-08-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_alter_shoppinglist_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='items',
            field=models.ManyToManyField(blank=True, to='quickstart.ShopItem'),
        ),
    ]
