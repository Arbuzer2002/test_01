from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse


def index(request):
    return render(request, 'mysite/index.html')


def shop(request):
    products = Product.objects.all()
    return render(request, 'mysite/shop.html', {'products': products})


def page(request):
    return render(request, 'mysite/tast.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Замените 'home' на URL вашей домашней страницы
        else:
            error_message = 'Неверные учетные данные. Попробуйте еще раз.'
            return render(request, 'mysite/login.html', {'error_message': error_message})
    else:
        return render(request, 'mysite/login.html')


def logout_view(request):
    logout(request),
    return redirect('')  # Замените 'home' на URL вашей домашней страницы


def my_view(request):
    # Сохранение значения переменной сеанса
    request.session['my_variable'] = 'my_value'

    # Получение значения переменной сеанса
    my_variable = request.session.get('my_variable')

    return render(request, 'my_template.html', {'my_variable': my_variable})
