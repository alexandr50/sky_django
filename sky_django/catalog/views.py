from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from catalog.forms import ContactForm


def home(request):
    return render(request, 'catalog/home.html')



def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('catalog:thanks'))
        else:
            pass
    else:
        form = ContactForm()

    return render(request, 'catalog/contacts.html', {'form': form})

def thanks(request):
    return render(request, 'catalog/thanks.html')