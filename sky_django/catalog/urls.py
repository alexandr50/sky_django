from django.urls import path

from catalog.views import home, contacts, detail_product, create_product

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('detail_product/<int:id>/', detail_product, name='detail_product'),
    path('create_product/', create_product, name='create_product')
]
