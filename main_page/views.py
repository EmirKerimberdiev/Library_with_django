from django.contrib import admin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from . import models
import datetime


# Search button
class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books_list'
    paginate_by = 10

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# book_list with class
@method_decorator(cache_page(60 * 15), name='dispatch')
class BooksListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books_list'
    model = models.Books

    def get_queryset(self):
        return self.model.objects.select_related().order_by('-id')


# detail_book with class
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)


# def books_list_view(request):
#     if request.method == 'GET':
#         books_list = models.Books.objects.filter().order_by('-id')
#         context = {'books_list': books_list}
#         return render(request, template_name='book.html', context=context)
#
#
# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id)
#         context = {'book_id': book_id}
#         return render(request, template_name='book_detail.html', context=context)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse("👨‍💻Hello! My name is Emir and I am a would-be a Backend Developer👨‍💻.")


def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse(
            "<img src='https://myfavoritepets.ru/wp-content/uploads/news373_1.jpg'>- This is my parrot, Grigoriy", )


def system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())
