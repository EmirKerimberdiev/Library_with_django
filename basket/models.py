from django.db import models
from main_page.models import Books


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя заказчика")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(blank=True, null=True, verbose_name="Электронная почта")
    book = models.ForeignKey(Books, on_delete=models.CASCADE,  verbose_name='Книга')

    def __str__(self):
        return f"{self.name} - {self.book}"

