from django.shortcuts import render
from app.settings.models import Category, Product, ProductImage

# Create your views here.
def index(request):
    category_all = Category.objects.all()
    product_image_all = ProductImage.objects.all()
    product_all = Product.objects.all()[:8]
    product2_all = Product.objects.all()[:3]
    return render(request, 'index.html', locals())

