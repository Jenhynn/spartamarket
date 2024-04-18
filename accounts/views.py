from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    pass


def logout(request):
    pass