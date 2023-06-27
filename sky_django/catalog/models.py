from django.db import models
from transliterate import translit

from users.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель')
    title = models.CharField(max_length=20, verbose_name='Назавание')
    description = models.CharField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='media', verbose_name='Изображение', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False, verbose_name='опубликованно')

    def __str__(self):
        return f'{self.title} | {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


        permissions = [
                (
                    'set_published',
                    'Can publish products'
                )
            ]


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.FloatField(verbose_name='Номер версии')
    name_version = models.CharField(max_length=30, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Активная')

    def save(self, *args, **kwargs):
        versions = Version.objects.filter(product_id=self.product.id)
        for version in versions:
            if version.is_active == True:
                raise ValueError('У продукта уже есть активная версия')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.title}  {self.name_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='Категория')
    description = models.CharField(max_length=300, verbose_name='Описание')

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Contact(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField()
    site = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.phone} | {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    slug = models.CharField(max_length=30, verbose_name='Слаг')
    content = models.TextField(verbose_name='Контент')
    preview = models.ImageField(upload_to='media', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=False, verbose_name='Опубликованно')
    count_views = models.IntegerField(default=0, verbose_name='Коллчество просмотров')

    def save(self, *args, **kwargs):
        self.slug = translit(self.title, language_code='ru', reversed=True)
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.is_published = False
        self.save()

    def __str__(self):
        return f'{self.title} | {self.content[:30]}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
