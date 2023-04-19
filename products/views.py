from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(
        request,
        'index.html',
        context={'products': products}
    )


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(
        request,
        'detail.html',
        context={'product': product})


def form(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products')
    else:
        form = ProductForm()

    return render(
        request,
        'product_form.html',
        {'form': form}
    )
