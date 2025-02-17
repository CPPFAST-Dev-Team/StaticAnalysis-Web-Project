from rest_framework import serializers
from .models import Project, Vulnerability

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

    This serializer handles the conversion between Project instances and their JSON representations.
    """
    class Meta:
        model = Project
        fields = '__all__'

class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = '__all__'