# urls.py 

from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('accounts/', views.accounts),
]