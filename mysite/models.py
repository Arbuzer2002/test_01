from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


class Material(models.Model):
    name = models.CharField(max_length=64)


class Color(models.Model):
    name = models.CharField(max_length=64)


class Gender(models.Model):
    name = models.CharField(max_length=64)


class Brand(models.Model):
    name = models.CharField(max_length=64)


class Size(models.Model):
    name = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)


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
