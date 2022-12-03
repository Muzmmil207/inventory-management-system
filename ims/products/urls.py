from django.urls import include, path

from . import views

urlpatterns = [
    path("categories/", views.categories, name="categories"),
    path("categories/<slug:slug>/", views.product_by_category, name="category"),
    path("api/", include("products.api.urls")),
]
