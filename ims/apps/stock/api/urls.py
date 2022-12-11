from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.ProductAPIView.as_view(), name="products_api"),
    path("category/", views.CategoryAPIView.as_view(), name="categories_api"),
    path(
        "category/<slug:slug>/",
        views.ProductByCategoryAPIView.as_view(),
        name="category_api",
    ),
    path(
        "p/<str:id>/",
        views.SingleProductAPIView.as_view(),
        name="product_api",
    ),
]
