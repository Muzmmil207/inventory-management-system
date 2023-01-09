from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class Categories(LoginRequiredMixin, TemplateView):
    template_name = "products/categories.html"


class ProductByCategory(LoginRequiredMixin, TemplateView):
    template_name = "products/product_by_category.html"


class ProductDetail(LoginRequiredMixin, TemplateView):
    template_name = "products/product_detail.html"
