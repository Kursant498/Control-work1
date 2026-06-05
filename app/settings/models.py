from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    logo = models.ImageField(
        upload_to="category/", 
        verbose_name="Логотип категории"
    )
    title = models.CharField(
        max_length=155, 
        verbose_name="Название категории"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class ProductImage(models.Model):
    image = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение людей"
    )

    class Meta:
        verbose_name = "Изображение человек"
        verbose_name_plural = "Изображения людей"

class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        verbose_name="Категория товара"
    )
    title = models.CharField(
        max_length=155, 
        verbose_name="Название товара"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Цена товара"
    )
    
    description = RichTextField(
        verbose_name="Описание товара"
    )
    image1 = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение товара"
    )
    image2 = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение товара"
    )
    image3 = models.ImageField(
        upload_to="product/", 
        verbose_name="Изображение товара"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания товара"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"