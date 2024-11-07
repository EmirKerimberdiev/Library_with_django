from django.contrib import admin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
import datetime


def books_list_view(request):
    if request.method == 'GET':
        books_list = models.Books.objects.filter().order_by('-id')
        context = {'books_list': books_list}
        return render(request, template_name='book.html', context=context)

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)




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