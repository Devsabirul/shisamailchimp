from django.db import models


class EmailAdd(models.Model):
    email = models.EmailField(max_length=250)
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class MessageSendHistory(models.Model):
    message = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
