from django.urls import path
from . import views

urlpatterns = [
    path('', views.ru_index, name='index'),
    path('index', views.ru_index, name='index'),
    path('ru_new', views.ru_new, name='ru_new'),
    path('ru_offers', views.ru_offers, name='ru_offers'),
    path('ru_search', views.ru_search, name='ru_search'),
    path('ru_test', views.ru_test, name='ru_test'),
    path('en_main', views.en_main, name='en_main'),
    path('news1', views.news1, name='news1'),
    path('news2', views.news2, name='news2'),
    path('news3', views.news3, name='news3'),
    path('year_products', views.year_products, name='year_products'),
    path('colour_products', views.colour_products, name='colour_products'),
    path('model_products', views.brand_products, name='model_products'),
    path('men_products', views.men_products, name='men_products'),
    path('type_products', views.type_products, name='type_products'),
    path('woman_products', views.woman_products, name='woman_products'),
]
