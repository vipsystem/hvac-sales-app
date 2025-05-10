from rest_framework import serializers
from .models import HVACProduct

class HVACProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HVACProduct
        fields = '__all__'
