from django.urls import path
from . import views


urlpatterns = [
    # path('create_order/', views.create_order_view, name='create'),
    # path('order_list/', views.order_list_view, name='order_list'),
    # path('order_list/<int:id>/delete/', views.delete_order_view, name='delete_order'),
    # path('order_list/<int:id>/update/', views.update_order_view, name='update_order'),

    # path with class
    path('order_class/', views.OrderListView.as_view(), name='order_list_class'),
    path('order_class/<int:id>/update/', views.UpdateOrderView.as_view(), name='update'),
    path('order_class/<int:id>/delete/', views.DeleteOrderView.as_view(), name='delete'),
    path('create_order/', views.OrderCreateView.as_view(), name='create_class'),

]