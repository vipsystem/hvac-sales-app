from rest_framework import serializers
from .models import SalesUser

class SalesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'department']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = SalesUser.objects.create_user(**validated_data)
        return user
