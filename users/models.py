from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    level = models.CharField(max_length=20, default='Junior')
    salary = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.level == 'Junior':
            self.salary = 300
        elif self.level == 'Middle':
            self.salary = 1000
        elif self.level == 'Senior':
            self.salary = 2000
        else:
            self.salary = 'Неизвестный уровень'

        super().save(*args, **kwargs)
