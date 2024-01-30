from django.core.management.base import BaseCommand
from mysite.models import Product

class Command(BaseCommand):
    help = 'Adds products to the database'

    def handle(self, *args, **kwargs):
        products = [
            {
                'name': 'Product 1',
                'image': 'product_images/product1.jpg',
                'description': 'This is product 1',
                'category': 'Category 1',
                'size_s': True,
                'size_m': True,
                'size_l': False,
                'price': 10.99
            },
            {
                'name': 'Product 2',
                'image': 'product_images/product2.jpg',
                'description': 'This is product 2',
                'category': 'Category 2',
                'size_s': False,
                'size_m': True,
                'size_l': True,
                'price': 9.99
            },
            # Добавьте остальные товары с соответствующими полями размеров
        ]
        
        for product_data in products:
            product = Product.objects.create(**product_data)
            self.stdout.write(f"Added product: {product.name}")

