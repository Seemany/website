from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'products': products})


def about(request):
    return render(request, 'main/about.html')


def dobavlenie(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма плохая'

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/dobavlenie.html', context)