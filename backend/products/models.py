from django.db import models
from authentication.models import SalesUser

class HVACProduct(models.Model):
    CATEGORY_CHOICES = (
        ('ac', 'Air Conditioner'),
        ('heater', 'Heater'),
        ('heat_pump', 'Heat Pump'),
        ('ventilation', 'Ventilation System')
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    model_number = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    energy_efficiency_rating = models.CharField(max_length=10, blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.model_number}'
