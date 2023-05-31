from django.urls import path

from catalog.views import *

app_name = 'catalog'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('contacts/', ContactList.as_view(), name='contact_list'),
    path('contacts/create_contact', ContactCreate.as_view(), name='contact_create'),
    path('detail_product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('create_product/', ProductCreate.as_view(), name='product_form'),
    path('post_list/', PostList.as_view(), name='post_list'),
    path('detail_post/<int:pk>/', DetailPost.as_view(), name='post_detail'),
    path('create_post/', PostCreate.as_view(), name='post_form'),
    path('update_post/<int:pk>/', PostUpdate.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', DeletePost.as_view(), name='delete_post'),
]
