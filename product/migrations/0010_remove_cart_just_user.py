# Generated by Django 4.2.4 on 2023-08-21 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_rename_user_cart_just_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='just_user',
        ),
    ]