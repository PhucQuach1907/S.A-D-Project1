from django.shortcuts import render
from .models import Product

# Create your views here.
def show_product(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'product.html', {'products': products})