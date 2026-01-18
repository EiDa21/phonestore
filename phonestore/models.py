from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     image = models.ImageField(upload_to='images')

class Contact(models.Model):
    name = models.CharField(max_length= 500)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.TextField()

# Create your models here.
