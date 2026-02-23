from django.contrib import admin
from .models import Flower

# Register your models here.
@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ['flower_name', 'flower_quantity', 'flower_price']

