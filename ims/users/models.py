from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from products.models import Address

from .managers import CustomUserManager


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(db_index=True, max_length=150)
    last_name = models.CharField(max_length=150)
    country = CountryField()
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
    profile = models.OneToOneField(
        "Profile", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    GENDER_SELECT = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=200, choices=GENDER_SELECT)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

    class Meta:
        indexes = [
            models.Index(fields=["first_name"]),
        ]
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Profile(models.Model):
    description = models.TextField()
