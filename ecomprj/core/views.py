from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product, Category, Vendor, CartOrder, Wishlist, CartOrderItems, ProductImages, ProductReview, Address


# Create your views here.

def index(request):
    products = Product.objects.all().order_by("-id")

    context={
        "products" : products
    }
    return render(request, 'core/index.html', context)