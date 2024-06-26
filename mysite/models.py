import datetime

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    sizes = models.ManyToManyField(Size)
    is_new = models.BooleanField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_date = models.DateTimeField(default=timezone.now)
    is_recommend = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FeaturedProduct(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='featured_products_images/')
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=7))

    def __str__(self):
        return self.name


class UniqueProduct(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='unique_products_images/')
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=7))

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
