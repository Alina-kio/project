# Generated by Django 4.2.4 on 2023-08-21 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True)),
                ('oredered', models.BooleanField(default=False)),
                ('total_price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('assembly_required', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, max_length=500, null=True)),
                ('depth', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('package_length', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('package_height', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('package_width', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('default_delivery_price', models.DecimalField(blank=True, decimal_places=2, default=5.0, max_digits=10)),
                ('default_delivery_time', models.IntegerField(blank=True, default=5)),
                ('created', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
                ('image', models.ManyToManyField(related_name='products', to='product.productimage')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('total_items', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
