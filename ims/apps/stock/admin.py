from django.contrib import admin

from .models import (
    Address,
    Brand,
    Category,
    Media,
    Product,
    ProductInventory,
    ProductType,
    Supplier,
)

admin.site.register(Address)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Media)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(Supplier)
