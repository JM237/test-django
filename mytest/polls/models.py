from django.db import models

# Create your models here.

class user(models.Model):
    user_login = models.CharField(max_length=30)
    user_password = models.CharField(max_length=8)

