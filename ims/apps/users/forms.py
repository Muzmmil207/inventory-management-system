from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import EmailInput, PasswordInput, Select, TextInput

from .models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "email"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "password"}
        )


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "required": "required",
            }
        )
    )
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
                "required": "required",
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "country",
            "mobile_number",
            "gender",
        )

        widgets = {
            "username": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username",
                    "required": "required",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "E-mail Address",
                    "required": "required",
                }
            ),
            "first_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name",
                    "required": "required",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name",
                    "required": "required",
                }
            ),
            "country": Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Country",
                    "required": "required",
                }
            ),
            "mobile_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Mobile Number",
                    "required": "required",
                }
            ),
            "gender": Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Gender",
                    "required": "required",
                }
            ),
        }
