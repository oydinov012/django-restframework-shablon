
from rest_framework import serializers
from apps.product.models import Product


class ProductRequestSerializer(serializers.Serializer):
    product_code = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate_product_code(self, value):
        if not Product.objects.filter(product_code=value).exists():
            raise serializers.ValidationError(
                f"{value} kodli mahsulot topilmadi"
            )
        return value