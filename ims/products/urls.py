from django.urls import include, path

from .views import Categories, ProductByCategory, ProductDetail

urlpatterns = [
    path("categories/", Categories.as_view(), name="categories"),
    path(
        "categories/<slug:slug>/",
        ProductByCategory.as_view(),
        name="category",
    ),
    path(
        "<slug:slug>/",
        ProductDetail.as_view(),
        name="product",
    ),
    path("api/", include("products.api.urls")),
]
