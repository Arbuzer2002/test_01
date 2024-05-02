from django.db.models import Sum, Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand, News, FeaturedProduct


def home(request):
    news = News.objects.all().order_by('-date')
    latest_products = Product.objects.all().order_by('-added_date')[:5]
    featured_products = FeaturedProduct.objects.all().order_by('-release_date')[:5]

    return render(request, 'mysite/home.html', {'news': news, 'latest_products': latest_products,
                                                'featured_products': featured_products})


def quick_view(request):
    product_id = request.GET.get('product_id')
    if product_id:
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'mysite/quick_view.html', {'product': product})


def feat_quick_view(request):
    product_id = request.GET.get('product_id')
    if product_id:
        product = get_object_or_404(FeaturedProduct, pk=product_id)
        return render(request, 'mysite/quick_view.html', {'product': product})


def shop(request):
    sort_by = request.GET.get('sort_by', 'default')
    search_query = request.GET.get('search', '')

    products = Product.objects.all()

    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    if sort_by == 'name_asc':
        products = products.order_by('name')
    elif sort_by == 'name_desc':
        products = products.order_by('-name')
    elif sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')

    category_name = request.GET.get('category', 'all')
    if category_name == "all":
        products = products.all()
    else:
        products = products.filter(category__name=category_name)

    brand_name = request.GET.get('brand', 'all')
    if brand_name == "all":
        products = products.all()
    else:
        products = products.filter(brand__name=brand_name)

    price_range = request.GET.get('price_range', '0')
    if price_range == "0":
        products = products.all
    else:
        min_price, max_price = price_range.split('-')
        products = products.filter(price__gte=min_price, price__lte=max_price)

    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(request, 'mysite/shop.html', {'products': products, 'categories': categories, 'brands': brands})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    total_sizes = product.sizes.aggregate(total=Sum('quantity'))['total']
    total_sizes = total_sizes if total_sizes is not None else 0
    return render(request, 'mysite/product_detail.html', {'product': product, 'total_sizes': total_sizes})


def page(request):
    return render(request, 'mysite/tast.html')
