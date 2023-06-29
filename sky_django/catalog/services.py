from django.core.cache import cache

from catalog.models import Category
from sky_django.settings import CACHE_ENABLED


def get_categories():
    if CACHE_ENABLED:
        key = f'categories_list'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(categories_list, categories_list)
    else:
        categories_list = Category.objects.all()

    return categories_list