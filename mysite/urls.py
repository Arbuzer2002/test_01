from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index, name='home'),
    path('shop.html', views.shop, name='shop'),
    path('login/', views.login_view, name='login'),
    path('tast.html', views.page),
    path('logout/', views.logout_view, name='logout'),
]
