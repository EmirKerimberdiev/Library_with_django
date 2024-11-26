from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class CustomUser(User):
    LEVEL_CHOICES = (
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    )
    level = models.CharField(choices=LEVEL_CHOICES, default='Junior', max_length=10)
    salary = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.level == 'Junior':
            self.salary = 300
        elif self.level == 'Middle':
            self.salary = 1000
        elif self.level == 'Senior':
            self.salary = 2000
        else:
            self.salary = 0

        super().save(*args, **kwargs)
