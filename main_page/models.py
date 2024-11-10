from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Books(models.Model):
    GENRE_CHOICE = (
        ('Приключения', 'Приключения'),
        ('Книга рецептов', 'Книга рецептов'),
        ('Фентези', 'Фентези')
    )
    image = models.ImageField(upload_to='books/', verbose_name='загрузите картинку')
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    description = models.TextField(verbose_name='Напишите описание книги', default='Lorem Ipsum', null=True)
    price = models.FloatField(verbose_name='Укажите цену книги')
    date_published = models.DateField(verbose_name='Укажите дату публикации книги', null=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Приключения',
                             verbose_name='Укажите жанр книги')
    pages = models.CharField(max_length=50, verbose_name='Укажите количество страниц в книге')
    autor = models.CharField(max_length=30, verbose_name='Укажите автора книги')
    audio_book = models.URLField(verbose_name='Укажите ссылку на аудио-книгу')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}$'


class ReviewBooks(models.Model):
    review_books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews_books')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Напишите отзыв к книге')
    mark = models.PositiveIntegerField(verbose_name='Оцените книгу от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_books}-{self.created_at}'

    class Meta:
        verbose_name = 'Отзыв к книге'
        verbose_name_plural = 'Отзывы к книгам'
