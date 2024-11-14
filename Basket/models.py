from django.db import models



class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя заказчика')
    phone = models.CharField(max_length=20, verbose_name='Введите номер телефона')
    email = models.EmailField(verbose_name='Введите email')
    book = models.CharField(max_length=200, verbose_name='Введите адрес доставки')



