from rest_framework import serializers
from .models import Burger

class BurgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = ['name', 'image', 'price', 'type']
