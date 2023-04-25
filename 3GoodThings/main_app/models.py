from django.db import models
from django.contrib.auth.models import User
from django import forms  


class User(models.Model):
    name = models.CharField(max_length=100)
    email = forms.EmailField(max_length=200, help_text='Required')  

class EmailVerification(models.Model):
    email = models.EmailField()
    verification_code = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)