# urls.py 

from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/edit/', views.edit, name='edit'),

]