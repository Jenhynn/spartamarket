from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 50)
    price = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.content
    