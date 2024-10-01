from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name