from django.db import models
from authentication.models import SalesUser
from products.models import HVACProduct

class SalesQuote(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('sent', 'Sent to Customer'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    )

    sales_rep = models.ForeignKey(SalesUser, on_delete=models.SET_NULL, null=True)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    quote_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Quote for {self.customer_name} - {self.quote_date}'

class SalesQuoteItem(models.Model):
    quote = models.ForeignKey(SalesQuote, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(HVACProduct, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.unit_price = self.product.price
        super().save(*args, **kwargs)
        # Update total amount of the quote
        self.quote.total_amount = sum(
            item.quantity * item.unit_price 
            for item in self.quote.items.all()
        )
        self.quote.save()
