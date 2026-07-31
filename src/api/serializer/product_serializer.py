from rest_framework import serializers
from apps.product.models import Product, Warehouse, Material, ProductMaterial


class ProductSerializer(serializers.Serializer):
    