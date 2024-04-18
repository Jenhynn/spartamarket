from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

def users(request):
    return render(request, "users.html")



# 프로필 조회
def profile(request, id):
    member = get_object_or_404(get_user_model(), id=id)
    context = {"member" : member}
    return render(request, "users/profile.html", context)
