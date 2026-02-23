from django.db import models

# Create your models here.
class Flower(models.Model):
    flower_name = models.CharField(max_length=100)
    flower_quantity = models.IntegerField()
    flower_price = models.DecimalField(max_digits=10, decimal_places=2)