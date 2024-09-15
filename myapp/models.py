from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField(default = now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.category
    
    class Meta:
        ordering = ['-date']

    
class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Income(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    date = models.DateField(default = now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    source = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return self.source
    
    class Meta:
        ordering = ['-date']

class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name