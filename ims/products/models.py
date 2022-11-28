import uuid

from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from users.models import User


class Category(MPTTModel):
    """
    Inventory Category table implemented with MPTT
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

    name = models.CharField(
        max_length=100,
        verbose_name=_("Name"),
        help_text=_("The product name to be displayed on the Inventory."),
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


class ProductInventory(models.Model):
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
        "Supplier",
        on_delete=models.CASCADE,
        related_name="supplier_inventory",
        verbose_name=_("Supplier"),
        help_text=_(
            "The supplier id to identify the supplier associated with the inventory item."
        ),
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="user",
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
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        verbose_name=_("price"),
        help_text=_("The price at which the product was purchased."),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        verbose_name=_("Discount"),
        help_text=_("The discount is given by the supplier."),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name=_("quantity"),
        help_text=_("The total quantity received at the inventory.ier."),
    )
    sold = models.PositiveIntegerField(
        default=0,
        verbose_name=_("sold"),
        help_text=_("The total quantity sold to the customers."),
    )
    available = models.IntegerField(
        default=0,
        verbose_name=_("Available"),
        help_text=_("The quantity that is available on the stock."),
    )
    defective = models.IntegerField(
        verbose_name=_("Defective"),
        help_text=_(
            "The total defective items either received at the inventory or returned by the customers."
        ),
    )

    class Meta:
        verbose_name = _("Product Inventory")
        verbose_name_plural = _("Products Inventory")

    def __str__(self):
        return self.product


class Media(models.Model):
    """
    The product image table.
    """

    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media_product_inventory",
    )
    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product image"),
        upload_to="images/",
        default="images/default.png",
        help_text=_("format: required, default-default.png"),
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("alternative text"),
        help_text=_("format: required, max-255"),
    )
    is_feature = models.BooleanField(
        default=False,
        verbose_name=_("product default image"),
        help_text=_("format: default=false, true=default image"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("product visibility"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date sub-product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")


class Address(models.Model):
    """
    Address Tabe
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.CharField(_("Phone Number"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    address_line = models.CharField(_("Address Line 1"), max_length=255)
    address_line2 = models.CharField(_("Address Line 2"), max_length=255)
    town_city = models.CharField(_("Town/City/State"), max_length=150)
    delivery_instructions = models.CharField(
        _("Delivery Instructions"), max_length=255
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "Address"


class Supplier(models.Model):
    """
    Product details table
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("Name"),
        help_text=_("Supplier name."),
    )
    address = models.OneToOneField(
        Address, on_delete=models.SET_NULL, null=True, blank=True
    )
    phone_regex = RegexValidator(
        regex=r"^(?:\+249|0)?(01\d{8})$",
        message=_(
            "Phone number must be entered in the format: `+24901XXXXXXXX`."
        ),
    )
    mobile_number = models.CharField(
        validators=[phone_regex],
        max_length=20,
        unique=True,
        verbose_name=_("Mobile Number"),
    )
    email_regex = RegexValidator(
        regex=r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$",
        message=_("Email must be entered in the format: `abc@abc.com`."),
    )
    email = models.EmailField(
        validators=[email_regex],
        unique=True,
        verbose_name=_("E-mail"),
        error_messages={
            "unique": "Please use another Email, this is already exists.",
        },
    )
    other_details = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
