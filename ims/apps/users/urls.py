from django.urls import include, path

from . import views

urlpatterns = [
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("logout/", views.LogoutPageView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
]
