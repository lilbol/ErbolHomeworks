from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_day = models.DateTimeField(auto_now_add=True)
    updated_day = models.DateTimeField(auto_now=True)