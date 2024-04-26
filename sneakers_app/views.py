from django.shortcuts import render

from mysite.models import Product, Brand, Category, Color, Gender, FeaturedProduct


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
    featured_products = FeaturedProduct.objects.all()

    return render(request, 'sneakers_app/1news.html', {'featured_products': featured_products})


def news2(request):
    return render(request, 'sneakers_app/1news2.html')


def news3(request):
    return render(request, 'sneakers_app/1news3.html')


def year_products(request):
    all_years = Product.objects.values_list('year', flat=True).distinct()

    products_by_year = {}
    for year in all_years:
        products_by_year[year] = Product.objects.filter(year=year)

    return render(request, 'sneakers_app/1yearproducts.html', {'products_by_year': products_by_year})


def colour_products(request):
    all_colors = Color.objects.all()

    products_by_color = {}
    for color in all_colors:
        products_by_color[color] = Product.objects.filter(color=color)

    return render(request, 'sneakers_app/4colour.html', {'products_by_color': products_by_color})


def brand_products(request):
    all_brands = Brand.objects.all()

    products_by_brand = {}
    for brand in all_brands:
        products_by_brand[brand] = Product.objects.filter(brand=brand)

    return render(request, 'sneakers_app/2modelproducts.html', {'products_by_brand': products_by_brand})


def men_products(request):
    male_gender = Gender.objects.get(name='Male')
    unisex_gender = Gender.objects.get(name='Unisex')

    male_products = Product.objects.filter(gender=male_gender)
    unisex_products = Product.objects.filter(gender=unisex_gender)

    products_by_men = {
        'Мужское': male_products,
        'Унисекс': unisex_products
    }

    return render(request, 'sneakers_app/5menproducts.html', {'products_by_men': products_by_men})


def type_products(request):
    all_categories = Category.objects.all()

    products_by_category = {}
    for category in all_categories:
        products_by_category[category] = Product.objects.filter(category=category)

    return render(request, 'sneakers_app/3typeproducts.html', {'products_by_category': products_by_category})


def woman_products(request):
    female_gender = Gender.objects.get(name='Female')
    unisex_gender = Gender.objects.get(name='Unisex')

    female_products = Product.objects.filter(gender=female_gender)
    unisex_products = Product.objects.filter(gender=unisex_gender)

    products_by_women = {
        'Женское': female_products,
        'Унисекс': unisex_products
    }
    return render(request, 'sneakers_app/6womanproducts.html', {'products_by_women': products_by_women})
