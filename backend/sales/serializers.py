from rest_framework import serializers
from .models import SalesQuote, SalesQuoteItem
from products.serializers import HVACProductSerializer

class SalesQuoteItemSerializer(serializers.ModelSerializer):
    product = HVACProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SalesQuoteItem
        fields = ['id', 'product', 'product_id', 'quantity', 'unit_price']

class SalesQuoteSerializer(serializers.ModelSerializer):
    items = SalesQuoteItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = SalesQuote
        fields = ['id', 'sales_rep', 'customer_name', 'customer_email', 
                  'customer_phone', 'quote_date', 'status', 'total_amount', 'items']
        read_only_fields = ['quote_date', 'total_amount']

    def create(self, validated_data):
        items_data = self.context.get('request').data.get('items', [])
        quote = SalesQuote.objects.create(**validated_data)
        
        for item_data in items_data:
            SalesQuoteItem.objects.create(
                quote=quote, 
                product_id=item_data['product_id'], 
                quantity=item_data.get('quantity', 1)
            )
        
        return quote
