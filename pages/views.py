from django.shortcuts import render
from django.http import HttpResponse
from products.choices import price_choices, category_choices

from products.models import Product
from salesmanager.models import Salesmanager


def index(request):

    products = Product.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'products': products,
        'price_choices': price_choices,
        'category_choices': category_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    salesmanagers = Salesmanager.objects.order_by('-hire_date')

    context = {
        'salesmanagers': salesmanagers
    }

    return render(request, 'pages/about.html', context)
