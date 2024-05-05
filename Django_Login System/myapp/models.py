from django.db import models

# Create your models here.

class SignupForm(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class LoginForm(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name    