from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms


# READ
def order_list_view(request):
    if request.method == 'GET':
        order_list = models.Order.objects.filter().order_by('-id')
        return render(request, template_name='order/order_list.html', context={'order_list': order_list})


# EDIT
def update_order_view(request, id):
    order_id = get_object_or_404(models.Order, id=id)
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = forms.OrderForm(instance=order_id)
    return render(request, template_name='order/update_order.html', context={'form': form, 'order_id': order_id})


# DELETE
def delete_order_view(request, id):
    drop_order = get_object_or_404(models.Order, id=id)
    drop_order.delete()
    return redirect('order_list')


# create todo_
def create_order_view(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = forms.OrderForm()
    return render(request, template_name='order/create_order.html', context={'form': form})
