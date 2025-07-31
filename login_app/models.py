from django.db import models

# Create your models here.


class User_info(models.Model):
    email= models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email

class user_post(models.Model):
    author = models.CharField(max_length=256)
    post = models.CharField(max_length=256)
    
    def __str__(self):
        return self.author