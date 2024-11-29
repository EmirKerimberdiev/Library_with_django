from django.shortcuts import render
from . import models
from django.views import generic


class AllHashtagListView(generic.ListView):
    template_name = 'all_hashtags.html'
    context_object_name = 'hashtags_list'
    model = models.Hashtag

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class GrandHashtagListView(generic.ListView):
    template_name = 'grand.html'
    context_object_name = 'grand'
    model = models.Hashtag

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Для стариков').order_by('-id')


class YoungHashtagListView(generic.ListView):
    template_name = 'young.html'
    context_object_name = 'young'
    model = models.Hashtag

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Для молодых').order_by('-id')


class ChildrenHashtagListView(generic.ListView):
    template_name = 'children.html'
    context_object_name = 'children'
    model = models.Hashtag

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Для детей').order_by('-id')
