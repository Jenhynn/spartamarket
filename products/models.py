from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 50)
    price = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
        )
    
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add= True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_author"
        )

    def __str__(self):
        return self.content
    