from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import models


class DeviceListView(generic.ListView):
    template_name = 'mobile_devices/device_list.html'
    context_object_name = 'device_list'
    model = models.Device

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class DeviceDetailView(generic.DetailView):
    template_name = 'mobile_devices/device_detail.html'
    context_object_name = 'device'

    def get_object(self, **kwargs):
        device_id = self.kwargs.get('id')
        return get_object_or_404(models.Device, id=device_id)
