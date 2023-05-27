from django.core.paginator import Paginator
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from catalog.forms import ContactForm, CreateProductForm
from catalog.models import Product, Contact


def home(request):
    products = Product.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
    paginator = Paginator(products, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'title': 'Домашняя страница'}
    return render(request, 'catalog/home.html', context)

def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('catalog:home')
    else:
        form = CreateProductForm()
    context = {'form': form, 'title': 'Создание продукта'}

    return render(request, 'catalog/create_product.html', context)


def contacts(request):
    contacts = Contact.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('catalog:thanks'))
        else:
            pass
    else:
        form = ContactForm()
    context = {'contacts': contacts, 'form': form}

    return render(request, 'catalog/contacts.html', context)


def detail_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'catalog/detail_product.html', {'product': product})



