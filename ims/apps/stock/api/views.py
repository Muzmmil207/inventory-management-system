from apps.stock.models import Category, Product
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import CategorySerializer, ProductSerializer


class CategoryAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    """
    API endpoint that returns all Categories
    """

    queryset = Category.objects.c
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)


class ProductByCategoryAPIView(APIView):
    """
    Return product by category
    """

    def get(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    """
    API endpoint that returns all products
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)


class SingleProductAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
):
    """
    API endpoint that returns single product
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
