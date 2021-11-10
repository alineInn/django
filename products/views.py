from django.shortcuts import render, redirect
from .forms import ProductsForm
from .models import Product

# Convenção:


def home(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'products': product})


def form(request):
    data = {}
    data['form'] = ProductsForm()
    return render(request, 'form.html', data)


def create(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Product.objects.get(pk=pk)
    return render(request, 'view.html', data)