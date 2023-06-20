from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=30, unique=True, verbose_name='Почта')
    verify_code = models.CharField(max_length=10, unique=True, verbose_name='Код верификации')
    avatar = models.ImageField(upload_to='users', verbose_name='аватар', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    country = models.CharField(max_length=30, verbose_name='Страна', blank=True, null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'
