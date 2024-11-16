# Generated by Django 5.1.2 on 2024-11-10 17:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_alter_books_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='pages',
            field=models.CharField(max_length=50, verbose_name='Укажите количество страниц в книге'),
        ),
        migrations.CreateModel(
            name='ReviewBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Напишите отзыв к книге')),
                ('mark', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оцените книгу от 1 до 5')),
                ('review_books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_books', to='main_page.books')),
            ],
            options={
                'verbose_name': 'Отзыв к книге',
                'verbose_name_plural': 'Отзывы к книгам',
            },
        ),
    ]
