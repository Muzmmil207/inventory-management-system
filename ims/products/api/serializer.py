from rest_framework import serializers

from products.models import (
    Address,
    Brand,
    Category,
    Media,
    Product,
    ProductInventory,
    ProductType,
    Supplier,
)


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "type",
            "slug",
            "summary",
            "created_at",
            "updated_at",
            "content",
        ]
