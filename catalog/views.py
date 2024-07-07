from django.shortcuts import render, get_object_or_404
from .models import Category, Flower

def home(request):
    categories = Category.objects.all()
    return render(request, 'catalog/home.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    flowers = category.flowers.all()
    return render(request, 'catalog/category_detail.html', {'category': category, 'flowers': flowers})

def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    return render(request, 'catalog/flower_detail.html', {'flower': flower})
