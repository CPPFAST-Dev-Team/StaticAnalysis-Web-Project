from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    #owner_username = serializers.SerializerMethodField()
    #optional field to display the owner's username, custom method custom serialization logic
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'repository_url', 'owner', 'owner_username', 'created_at', 'updated_at', 'users']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    #def get_owner_username(self, obj):
    #    return obj.owner.username
