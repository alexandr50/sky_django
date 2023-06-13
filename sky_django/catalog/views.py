from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ContactForm, PostForm, CreateProductForm, UpdateProductForm, VersionForm
from catalog.models import Product, Contact, Post, Version
from catalog.service import send_email


class ProductList(ListView):
    model = Product
    extra_context = {
        'title': 'Список продуктов'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for item in context['object_list']:
        #     print(item.pk)
        #     context['version'] = Version.objects.filter(product_id=item.pk)

        return context

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'catalog/update_product.html'
    form_class = CreateProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.kwargs['pk']})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormset(data=self.request.POST, instance=self.object)
        else:
            context['formset'] = VersionFormset(instance=self.object)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)



class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    form_class = CreateProductForm

    def form_valid(self, form):
        form = CreateProductForm(data=self.request.POST)
        if form.is_valid():
            form.save()


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.filter(product_id=self.kwargs['pk'])
        for item in context['version']:
            if item.is_active == True:
                context['version'] = item
        return context




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