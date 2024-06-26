from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from products.models import Product

def users(request):
    return render(request, "users.html")



# 프로필 조회
def profile(request, id):
    member = get_object_or_404(get_user_model(), id=id)
    product = Product.objects.all().filter(author_id = id)
    liked = Product.objects.all().filter(like_users =id)
    print(liked)
    context = {
        "member" : member,
        "products": product,
        "liked_products": liked,
        }
    return render(request, "users/profile.html", context)


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk = user_id)
        if member != request.user:
            if member.followers.filter(pk = request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", id=member.id)
    else:
        return redirect("accounts:login")