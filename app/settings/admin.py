from django.contrib import admin

# Register your models here.
from app.settings.models import Category, ProductImage

admin.site.register(Category)
admin.site.register(ProductImage)