from django.urls import path
from mobile_devices import views

urlpatterns = [
    path('devices_list/', views.DeviceListView.as_view(), name='devices_list'),
    path('devices_detail/<int:id>/', views.DeviceDetailView.as_view(), name='devices_detail'),
]
