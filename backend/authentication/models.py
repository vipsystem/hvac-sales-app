from django.contrib.auth.models import AbstractUser
from django.db import models

class SalesUser(AbstractUser):
    ROLE_CHOICES = (
        ('sales_rep', 'Sales Representative'),
        ('manager', 'Sales Manager'),
        ('admin', 'Administrator')
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='sales_rep')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'
