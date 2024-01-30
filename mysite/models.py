from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    category = models.CharField(max_length=100)
    size_s = models.BooleanField(default=False, verbose_name='Size S')
    size_m = models.BooleanField(default=False, verbose_name='Size M')
    size_l = models.BooleanField(default=False, verbose_name='Size L')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
# Create your models here.
