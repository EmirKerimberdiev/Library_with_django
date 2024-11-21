from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.views import generic


# READ with class
class OrderListView(generic.ListView):
    template_name = 'order/order_list.html'
    context_object_name = 'order_list'
    model = models.Order

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


# CREATE with class
class OrderCreateView(generic.CreateView):
    form_class = forms.OrderForm
    template_name = 'order/create_order.html'
    success_url = '/order_class/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(OrderCreateView, self).form_valid(form=form)


# UPDATE with class
class UpdateOrderView(generic.UpdateView):
    template_name = 'order/update_order.html'
    form_class = forms.OrderForm
    success_url = '/order_class/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.Order, id=order_id)


# DELETE with class
class DeleteOrderView(generic.DeleteView):
    template_name = 'order/confirm_delete.html'
    success_url = '/order_class/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.Order, id=order_id)


# # READ
# def order_list_view(request):
#     if request.method == 'GET':
#         order_list = models.Order.objects.filter().order_by('-id')
#         return render(request, template_name='order/order_list.html', context={'order_list': order_list})
#
#
# # EDIT
# def update_order_view(request, id):
#     order_id = get_object_or_404(models.Order, id=id)
#     if request.method == 'POST':
#         form = forms.OrderForm(request.POST, instance=order_id)
#         if form.is_valid():
#             form.save()
#             return redirect('order_list')
#     else:
#         form = forms.OrderForm(instance=order_id)
#     return render(request, template_name='order/update_order.html', context={'form': form, 'order_id': order_id})
#
#
# # DELETE
# def delete_order_view(request, id):
#     drop_order = get_object_or_404(models.Order, id=id)
#     drop_order.delete()
#     return redirect('order_list')
#
#
# # create todo_
# def create_order_view(request):
#     if request.method == 'POST':
#         form = forms.OrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('order_list')
#     else:
#         form = forms.OrderForm()
#     return render(request, template_name='order/create_order.html', context={'form': form})
