from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import UserLoginForm, UserRegistrationForm


class LoginPageView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm


class LogoutPageView(LogoutView):
    next_page = "/users/login/"


@login_required
def register(request):
    form = UserRegistrationForm
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "users/registration.html", {"form": form})
