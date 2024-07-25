from rest_framework import serializers
from .models import Bike

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = (
        "id",
        "reference",
        "trademark",
        "model",
        "price",
        "image",
        "supplier",
        )