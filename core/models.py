from django.db import models
from django.contrib.auth.models import User


class EmailAdd(models.Model):
    email = models.EmailField(max_length=250)
    category = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.category


class MessageSendHistory(models.Model):
    message = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    topic = models.CharField( max_length=500,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

