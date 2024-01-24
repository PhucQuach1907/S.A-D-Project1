from django.shortcuts import render, get_object_or_404
from .models import Category

def show_category(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'category.html', {'categories': categories})
