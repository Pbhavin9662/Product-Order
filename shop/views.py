from django.shortcuts import render, redirect
from .models import *
from .forms import *
# from .filter import OrderFilter


def index(request):
    order = Order.objects.all()
    # id = order.order_set.all()
    # myFilter = OrderFilter(request.GET, queryset=id)
    # orders = myFilter.qs
    context = {'order': order}
    return render(request, "index.html", context)


def order(request):
    product = Product.objects.all()
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = OrderForm()
    context = {'form': form}
    return render(request, "product_form.html", context)


def update_order(request, pk):
    id = Order.objects.get(id=pk)
    form = OrderForm(instance=id)
    print("----", form)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, "product_form.html", context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('/')
    context = {}
    return render(request, 'index.html', context)
