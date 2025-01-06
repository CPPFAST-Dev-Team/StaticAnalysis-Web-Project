from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

    This serializer handles the conversion between Project instances and their JSON representations.
    """
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'repository_url', 'owner', 'created_at', 'updated_at', 'users']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']