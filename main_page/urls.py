from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]
