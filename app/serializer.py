from rest_framework import serializers
from .models import Vehicle, Vehicle_Model

class vehicle_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Model
        fields = '__all__'

class vehicle_serializer(serializers.ModelSerializer):
    vehicle_model_id = vehicle_model_serializer(read_only=True)
    class Meta:
        model = Vehicle
        fields = '__all__'
        depth = 1

class vehicle_create_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        exclude = ('created_on', 'last_modified')

