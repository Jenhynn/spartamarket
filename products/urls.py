# urls.py 

from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comment/', views.comment_create, name="comment_create"),
    path('<int:pk>/comment/<int:comment_id>/delete/', views.comment_delete, name="comment_delete"),
    path("<int:pk>/like", views.like, name="like")

]