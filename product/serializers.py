from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'price', 'default_delivery_price', 'default_delivery_time']


class ProductDetailSerializer(serializers.ModelSerializer):
    image = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'




