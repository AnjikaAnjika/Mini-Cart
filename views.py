from django.shortcuts import render
from .models import Product, Contact, Order
from math import ceil
# Create your views here.
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()

    print(products)
    n = len(products)
    print(n)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    print(nslides)
    params = {'no_of_slides': nslides, 'product': products, 'range': range(1, nslides)}
    return render(request, 'shop/index.html', {'product': products})
    # return render(request, 'shop/product.html', {'product': products})


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    phone = request.GET.get('phone', '')
    desc = request.GET.get('desc', '')
    print(name, email, phone, desc)
    con = Contact(caller=name, email=email, phone=phone, desc=desc)
    con.save()
    return render(request, "shop/contact.html")




def productview(request, myid):
    prod = Product.objects.filter(id=myid)
    print(prod)
    return render(request, 'shop/productview.html', {'prod': prod[0]})


def checkout(request):
    name = request.GET.get('name', '')
    email = request.GET.get('email', '')
    phone = request.GET.get('phone', '')
    address1 = request.GET.get('address1', '')
    address2 = request.GET.get('address2', '')
    state = request.GET.get('state', '')
    city = request.GET.get('city', '')
    zip = request.GET.get('zip', '')
    print(name, email, phone, address1, address2, state, city, zip)
    order = Order(name=name, email=email, phone=phone, address1=address1, address2=address2, state=state, city=city,
                  zip=zip)
    order.save()
    return render(request, 'shop/checkout.html')
