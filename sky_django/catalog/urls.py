from django.urls import path, include

from catalog.views import home, contacts

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
