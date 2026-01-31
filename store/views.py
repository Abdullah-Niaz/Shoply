from django.shortcuts import render, get_object_or_404

from category.models import Category
from .models import Product
# Create your views here.


def store(request, category_slug=None):
    products = None

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category,
            is_available=True
        )
    else:
        products = Product.objects.filter(is_available=True)

    context = {
        'products': products,
        'product_count': products.count(),
    }
    return render(request, "store/store.html", context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug,
            slug=product_slug, is_available=True)
    except Exception as e:
        raise e
    context = {'single_product': single_product}
    return render(request, 'store/product_detail.html', context)
