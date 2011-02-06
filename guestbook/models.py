from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()
