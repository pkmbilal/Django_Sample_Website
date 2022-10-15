from tabnanny import verbose
from django.db import models

# Create your models here.

class Services(models.Model):
    image = models.ImageField()
    service_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    btn_text = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Service'

class Portfolio(models.Model):
    image = models.ImageField()
    category = models.CharField(max_length=50)

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'