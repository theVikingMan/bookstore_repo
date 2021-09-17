from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=150)
    author      = models.CharField(blank=True, max_length=40)
    created     = models.DateField(null=True)
    summary     = models.TextField(default='Summary comming soon...')
    price       = models.DecimalField(max_digits=20, decimal_places=2)
    category    = models.CharField(max_length=100)
    picture     = models.ImageField(null=True)
    available   = models.BooleanField()