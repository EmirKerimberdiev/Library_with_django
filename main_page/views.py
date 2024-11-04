from django.contrib import admin
from django.http import HttpResponse
import datetime


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