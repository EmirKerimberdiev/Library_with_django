from django.urls import path
from . import views

urlpatterns = [
    path('books_list/', views.BookListView.as_view(), name='books_list'),
    path('books_parser/', views.BookFormView.as_view(), name='books_parser')
]