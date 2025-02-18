from rest_framework import serializers
from .models import Project, Vulnerability

class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'repository_url', 'owner', 'created_at', 'updated_at', 'users']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

class VulnerabilitySerializer(serializers.ModelSerializer):
    """
    Serializer for the Vulnerability model.
    
    Computes a color based on severity:
      LOW -> green, MEDIUM -> yellow, SEVERE -> red.
    """
    color = serializers.SerializerMethodField()

    class Meta:
        model = Vulnerability
        fields = ['id', 'project', 'name', 'file_location', 'line', 'vuln_id', 'severity', 'summary', 'confidence', 'color']

    def get_color(self, obj):
        severity_mapping = {
            "LOW": "green",
            "MEDIUM": "yellow",
            "SEVERE": "red"
        }
        # Use uppercase comparison to handle case variations.
        return severity_mapping.get(obj.severity.upper(), "unknown")