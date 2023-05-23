from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_lst = [
            {'title': 'Куртка', 'description': 'Осення куртка', 'price': 4000, 'category': Category.objects.get(title='Одежда')},
            {'title': 'Шапка', 'description': 'Осення шапка', 'price': 1000, 'category': Category.objects.get(title='Одежда')},
            {'title': 'Шарф', 'description': 'Шарф желтый', 'price': 500, 'category': Category.objects.get(title='Аксесуары')},
            {'title': 'Кросовки', 'description': 'Кросовки белые', 'price': 4000, 'category': Category.objects.get(title='Обувь')},
            {'title': 'Тапки', 'description': 'Тапки домашние', 'price': 400, 'category': Category.objects.get(title='Обувь')},
            {'title': 'Рюкзак', 'description': 'Рюкзак походный', 'price': 10000, 'category': Category.objects.get(title='Аксесуары')},
            {'title': 'Джинсы', 'description': 'Джинсы синие', 'price': 4000, 'category': Category.objects.get(title='Одежда')},
            {'title': 'Туфли', 'description': 'Туфли женские', 'price': 6000, 'category': Category.objects.get(title='Обувь')},
        ]

        products_for_append = []

        for product in products_lst:
            products_for_append.append(Product(**product))

        products_for_delete = Product.objects.all()
        if len(products_for_delete) > 0:
            for product in products_for_delete:
                product.delete()

        Product.objects.bulk_create(products_for_append)