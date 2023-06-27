from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ContactForm, PostForm, CreateProductForm, UpdateProductForm, VersionForm
from catalog.models import Product, Contact, Post, Version
from catalog.service import send_email


@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class UpdateProduct(UpdateView):
    model = Product
    template_name = 'catalog/update_product.html'
    form_class = UpdateProductForm
    # permission_required = 'catalog.change_product'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("Вы не являетесь владельцем продукта.")
        return obj




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

class ProductsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


    def test_func(self):
        return self.request.user.is_superuser




@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    form_class = CreateProductForm

    def form_valid(self, form):
        form = CreateProductForm(data=self.request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = self.request.user
            product.save()
        return HttpResponseRedirect(reverse('catalog:product_list'))


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



@method_decorator(login_required, name='dispatch')
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