from rest_framework import serializers
from .models import Product, Variant, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    variants = serializers.PrimaryKeyRelatedField(queryset=Variant.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'variants', 'features', 'created_on', 'updated_on', 'created_by', 'updated_by']
