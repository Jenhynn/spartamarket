from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import (AuthenticationForm,)
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from .forms import CustomUserCreationForm


# 로그인
def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login_auth(request, form.get_user())
            return redirect("signup")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "accounts/login.html", context)


# 로그아웃
def logout(request):
    pass


# 회원가입
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_auth(request, user)
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/signup.html", context)


# 회원 정보 수정
def update(request):
    pass


# 회원 탈퇴
def delete(request):
    pass


# 비밀번호 변경
def change_password(request):
    pass