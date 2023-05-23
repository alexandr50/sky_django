from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name='Назавание')
    description = models.CharField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

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

