from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'title': 'Одежда', 'description': 'Верхняя одежда разных брендов'},
            {"title": "Обувь", "description": "Обувь разных брендов"},
            {"title": "Аксесуары", "description": "Аксессуары"}
        ]

        category_for_append = []

        for category in category_list:
            category_for_append.append(Category(**category))

        lst = Category.objects.all()
        if len(lst) > 0:
            for item in lst:
                item.delete()
        Category.objects.bulk_create(category_for_append)


