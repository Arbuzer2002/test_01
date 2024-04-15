from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('tast', views.page),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
