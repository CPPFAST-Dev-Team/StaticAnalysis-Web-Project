from rest_framework import serializers
from .models import AnalysisResult

class AnalysisResultSerializer(serializers.ModelSerializer):
    """
    Serializer for the AnalysisResult model.

    This serializer handles the conversion between AnalysisResult instances and their JSON representations.
    """
    class Meta:
        model = AnalysisResult
        fields = ['id', 'project', 'timestamp', 'status', 'result']
        read_only_fields = ['id', 'project', 'timestamp', 'status', 'result']