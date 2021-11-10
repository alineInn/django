from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import ProductsForm
from .models import Product

# Convenção:


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def create(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST or None)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(reverse('view', kwargs={'pk': form.pk}))
    else:
        form = ProductsForm()

    return render(request, template_name='form.html', context={'form': form})


def view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'view.html', context={'db': product})