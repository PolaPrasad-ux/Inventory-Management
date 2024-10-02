from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InventoryItems(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name