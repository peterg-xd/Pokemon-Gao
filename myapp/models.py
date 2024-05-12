from django.db import models

# Create your models here.

class CardItem(models.Model):
    name = models.CharField(max_length = 200)
    obtained = models.BooleanField(default = False)