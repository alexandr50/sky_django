from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ContactForm, PostForm
from catalog.models import Product, Contact, Post
from catalog.service import send_email


class ProductList(ListView):
    model = Product
    extra_context = {
        'title': 'Список продуктов'
    }



class ProductCreate(CreateView):
    model = Product
    fields = ('title', 'description', 'image', 'price', 'category')
    success_url = reverse_lazy('catalog:product_list')


class ContactList(ListView):
    model = Contact
    extra_context = {
        'title': 'Контакты'
    }

class ContactCreate(CreateView):
    model = Contact

    form_class = ContactForm
    template_name = 'catalog/contact_create.html'
    success_url = reverse_lazy('catalog:contact_list')




class ProductDetail(DetailView):
    model = Product




class PostList(ListView):
    model = Post
    extra_context = {
        'title': 'Посты'
    }


class DetailPost(DetailView):
    model = Post
    
    def get_object(self, queryset=None):
        object = Post.objects.get(pk=self.kwargs['pk'])
        if object:
            object.count_views += 1
            object.save()
            if object.count_views == 100:
                send_email()
        return object

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('catalog:post_list')
    form_class = PostForm


class PostUpdate(UpdateView):
    model = Post
    template_name = 'catalog/update_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('catalog:post_detail', kwargs={'pk': self.kwargs['pk']})

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:post_list')