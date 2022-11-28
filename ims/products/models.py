from turtle import title

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from users.models import User


class Category(MPTTModel):
    """
    Inventory Category table implimented with MPTT
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: required, max-100"),
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )
    is_active = models.BooleanField(
        default=True,
    )
    content = models.TextField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_("The column used to store the category details."),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    The type to distinguish between the different product types.
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: required, max-100"),
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product details table
    """

    title = models.CharField(
        max_length=100,
        verbose_name=_("Title"),
        help_text=_("The product title to be displayed on the Inventory."),
    )
    category = TreeManyToManyField(
        Category, related_query_name="category", null=False, blank=False
    )
    type = models.ForeignKey(
        ProductType,
        related_name="product_type",
        on_delete=models.SET_NULL,
        null=True,
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name=_("Product safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )
    summary = models.TextField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Summary"),
        help_text=_("The summary to mention the key highlights."),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = RichTextField(
        max_length=1000,
        verbose_name=_("Content"),
        help_text=_(
            "The column used to store the additional details of the product."
        ),
    )

    def __str__(self):
        return self.title


class Brand(models.Model):
    """
    Brand table to store the brand data
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("Title"),
        help_text=_("The brand name to be displayed on the Inventory."),
    )

    def __str__(self):
        return self.name


class ProductsInventory(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_inventory",
        verbose_name=_("Product"),
        help_text=_(
            "The product id to identify the product associated with the inventory item."
        ),
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="brand_inventory",
        verbose_name=_("Brand"),
        help_text=_(
            "The brand id to identify the brand associated with the inventory item."
        ),
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="supplier_inventory",
        verbose_name=_("Supplier"),
        help_text=_(
            "The supplier id to identify the supplier associated with the inventory item."
        ),
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_inventory",
        verbose_name=_("Order"),
        help_text=_(
            "The order id to identify the order associated with the inventory item."
        ),
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Created By"),
        help_text=_(
            "The user id to identify the user who added the inventory item."
        ),
    )
    updated_By = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name=_("Updated By"),
        help_text=_(
            "The user id to identify the user who updated the inventory item."
        ),
    )
    sku = models.CharField(
        max_length=100,
        verbose_name=_("Stock Keeping Unit"),
        help_text=_("The id to identify the item on stock."),
    )
    mrp = models.FloatField(
        verbose_name=_("Maximum Retail Price"),
        help_text=_(
            "The printed price of the product associated with the item."
        ),
    )
    discount = models.FloatField(
        verbose_name=_("Discount"),
        help_text=_("The discount is given by the supplier."),
    )
    price = models.FloatField(
        verbose_name=_("price"),
        help_text=_("The price at which the product was purchased."),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("quantity"),
        help_text=_("The total quantity received at the inventory.ier."),
    )
    sold = models.PositiveIntegerField(
        verbose_name=_("sold"),
        help_text=_("The total quantity sold to the customers."),
    )
    available = models.FloatField(
        verbose_name=_("Available"),
        help_text=_("The quantity that is available on the stock."),
    )
    defective = models.FloatField(
        verbose_name=_("Defective"),
        help_text=_(
            "The total defective items either received at the inventory or returned by the customers."
        ),
    )

    def __str__(self):
        return self.product
