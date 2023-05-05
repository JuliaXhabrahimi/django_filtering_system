from rest_framework import serializers
from .models import Worker, ConstructionSite, Pylon, Job

# Define a serializer for the Worker model to handle serialization and deserialization
class WorkerSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serialized representation
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'email', 'user_type']

# Define a serializer for the ConstructionSite model to handle serialization and deserialization
class ConstructionSiteSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serialized representation
    class Meta:
        model = ConstructionSite
        fields = ['name']

# Define a serializer for the Pylon model to handle serialization and deserialization
class PylonSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serialized representation
    class Meta:
        model = Pylon
        fields = ['pylon_number', 'base_area', 'tip_surface', 'total_area']

# Define a serializer for the Job model to handle serialization and deserialization
class JobSerializer(serializers.ModelSerializer):
    # Specify the model and fields to include in the serialized representation
    class Meta:
        model = Job
        fields = ['worker', 'pylon', 'state', 'start_date', 'end_date', 'is_base_work']
