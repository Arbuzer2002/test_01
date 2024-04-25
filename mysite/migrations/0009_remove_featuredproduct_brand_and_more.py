# Generated by Django 5.0.4 on 2024-04-18 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_featuredproduct_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredproduct',
            name='brand',
        ),
        migrations.AlterField(
            model_name='featuredproduct',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 10, 19, 17, 561550)),
        ),
    ]