from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    price = models.FloatField(verbose_name='Price', null=True)
    date_of_purchase = models.DateField(verbose_name='Date of Purchase', null=True)
    image = models.ImageField(upload_to='device_images/', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Devices'


class ReviewDevice(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='reviews', null=True)
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Leave a review for the device', null=True)
    mark = models.PositiveIntegerField(
        verbose_name='Rate the device from 1 to 5',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f'{self.device} - {self.created_at}'  # Исправлено на 'device'

    class Meta:
        verbose_name_plural = 'Reviews'


CATEGORY_CHOICES = (
    ('Smartphones', 'Smartphones'),
    ('Tablets', 'Tablets'),
    ('Laptops', 'Laptops'),
    ('Accessories', 'Accessories'),
)


class Category(models.Model):
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.category


class Feature(models.Model):
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature
