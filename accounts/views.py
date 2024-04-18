from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm)
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm


def index(request):
    return render(request, "accounts/index.html")

# 로그인
@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login_auth(request, form.get_user())
            next_url = request.GET.get("next") or "accounts:index" # 로그인 후 이동 (기존에 접속하려고 했던 next 주소 또는 목록 페이지로) *** products:index로 바꾸기
            return redirect(next_url)
    else:
        form = AuthenticationForm() # POST method가 아닐 경우 (GET의 경우) Form 보여줌

    context = {"form": form} #context에 form 담아서 넘기기
    return render(request, "accounts/login.html", context) 


# 로그아웃 # html에서 로그인 되었을 때만 보이기
@require_POST
def logout(request):
    if request.user.is_authenticated:
        logout_auth(request)
    return redirect("accounts:index") # products:index로 redirect


# 회원가입
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) # 바인딩 된 폼
        if form.is_valid():
            user = form.save() # 폼 저장 후
            login_auth(request, user) # 로그인 해서
            return redirect("accounts:index") # products:index로 redirect
    else:
        form = CustomUserCreationForm() # GET 일 경우 회원가입 form 보여줌
    context = {
        "form": form
    }
    return render(request, "accounts/signup.html", context)


# 회원 정보 수정: html에서 로그인 된 회원 본인일 때만 회원 정보 수정 가능
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:index") # products:index로 redirect
    else:
        form = CustomUserChangeForm(instance = request.user)
    
    context = { "form": form}
    return render(request, "accounts/update.html", context)


# 회원 탈퇴 # html에서 로그인 된 회원 본인일 때만 보이기
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        logout_auth(request) # 세션을 지우기 위해 로그아웃 해주기
    return redirect("accounts:index") # product:index로 메인 화면으로 리다이렉트


# 비밀번호 변경
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST) # 상속 받은 SetPasswordForm이 self, user, *args, **kwargs 순서
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) 
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form" : form}
    return render(request, "accounts/change_password.html", context)
