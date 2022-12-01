from django.urls import include, path

from . import views

urlpatterns = [path("", views.ProductAPIView.as_view(), name="character_api")]
