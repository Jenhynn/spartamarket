from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from .forms import ProductForm, CommentForm
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/index.html", context)


def product_detail(request, pk): # pk 로 각 게시글의 상세 페이지 보기
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    comment_form = CommentForm()
    context = {
        "product": product,
        "comments": comments,
        "comment_form": comment_form,
    }
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


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect("products:index")


def comment_create(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit = False) # commit=False 를 해서 바로 저장하지 않음
        comment.product = product
        comment.save()
    return redirect("products:product_detail", pk)


def comment_delete(request, pk, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    comment.delete()
    return redirect("products:product_detail", pk)