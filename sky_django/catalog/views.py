from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from catalog.forms import ContactForm
from catalog.models import Product, Contact


def home(request):
    products = Product.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:5]
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


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


def thanks(request):
    return render(request, 'catalog/thanks.html')
