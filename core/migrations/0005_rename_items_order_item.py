# Generated by Django 4.1.7 on 2023-05-06 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_order_items_alter_order_order_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='item',
        ),
    ]
