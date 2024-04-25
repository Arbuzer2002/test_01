from django.shortcuts import render


def ru_index(request):
    return render(request, 'sneakers_app/rumain.html')


def ru_new(request):
    return render(request, 'sneakers_app/runew.html')


def ru_offers(request):
    return render(request, 'sneakers_app/ruoffers.html')


def ru_search(request):
    return render(request, 'sneakers_app/rusearch.html')


def ru_test(request):
    return render(request, 'sneakers_app/rutest.html')


def en_main(request):
    return render(request, 'sneakers_app/enmain.html')


def news1(request):
    return render(request, 'sneakers_app/1news.html')


def news2(request):
    return render(request, 'sneakers_app/1news2.html')


def news3(request):
    return render(request, 'sneakers_app/1news3.html')


def year_products(request):
    return render(request, 'sneakers_app/1yearproducts.html')


def colour_products(request):
    return render(request, 'sneakers_app/4colour.html')


def model_products(request):
    return render(request, 'sneakers_app/2modelproducts.html')


def men_products(request):
    return render(request, 'sneakers_app/5menproducts.html')


def type_products(request):
    return render(request, 'sneakers_app/3typeproducts.html')


def woman_products(request):
    return render(request, 'sneakers_app/6womanproducts.html')
