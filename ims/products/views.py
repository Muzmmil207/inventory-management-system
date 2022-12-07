from django.shortcuts import render
from django.views.generic import TemplateView


class Categories(TemplateView):
    template_name = "products/categories.html"


class ProductByCategory(TemplateView):
    template_name = "products/product_by_category.html"


class ProductDetail(TemplateView):
    template_name = "products/product_detail.html"
