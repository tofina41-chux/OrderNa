from django.shortcuts import render
from .models import Category, MenuItem, SliderImage

def index(request):
    categories = Category.objects.filter(is_active=True).prefetch_related('items')
    # Fetch all active custom slider images
    slides = SliderImage.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'menu/index.html', {'categories': categories, 'slides': slides})
    