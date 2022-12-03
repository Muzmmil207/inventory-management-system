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
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "is_active",
            "content",
            "parent",
        ]


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
