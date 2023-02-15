from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create your models here.
# class Users(models.Model):
#     email =models.EmailField(max_length=255,unique=True,primary_key=True)
#     first_name = models.CharField(max_length=255)
#     last_name=models.CharField(max_length=255)
#     password=models.CharField(max_length=255)


class User(AbstractUser):
    username = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Message(models.Model):
    body =models.TextField()
    author=models.ForeignKey(User,on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    target=models.ForeignKey(User,on_delete=models.PROTECT,related_name="target")