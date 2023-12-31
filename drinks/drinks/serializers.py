# serializers is going to describe the process of going from python object to json

from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
