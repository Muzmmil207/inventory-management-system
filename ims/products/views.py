from django.shortcuts import render


# Create your views here.
def categories(request):
    return render(request, "products/categories.html")

def product_by_category(request, slug):
    return render(request, "products/product_by_category.html", {'slug':slug})