from django.db import models
from django.contrib.auth.models import AbstractUser

# custom user model을 작성
class User(AbstractUser):
    following = models.ManyToManyField(
        'self', related_name="followers", symmetrical=False
        )