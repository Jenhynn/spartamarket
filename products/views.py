from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/index.html", context)


def product_detail(request, pk): # pk 로 각 게시글의 상세 페이지 보기
    product = get_object_or_404(Product, pk=pk)
    # Comment 작성한 것 보여주기
    # Comment Form 보여주기
    context = { "product": product}
    return render(request, "products/product_detail.html", context)


def create(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save()
        return redirect("products:product_detail", product.id)
    context = {"form" : form}
    return render(request, "products/create.html", context)


@require_http_methods(["GET", "POST"])
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            product = form.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm(instance = product)
    
    context = {
        "form" : form,
        "product": product,
    }
    return render(request, "products/edit.html", context)
