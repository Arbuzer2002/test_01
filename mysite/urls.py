from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('tast', views.page),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('get_quick_info/', views.quick_view, name='quick_view'),
]
