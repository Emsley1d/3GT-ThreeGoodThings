from django.db import models
from django import forms 
from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    email_verified = models.BooleanField(default=False)
    email_verification_code = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128, default='')
    last_login = models.DateTimeField(auto_now=True)


class EmailVerification(models.Model):
    email = models.EmailField()
    verification_code = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
