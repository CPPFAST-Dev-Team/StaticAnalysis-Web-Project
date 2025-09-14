from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer handles the conversion between User instances and their JSON representations.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user with the provided validated data.

        :param validated_data: The validated data for creating a new user.
        :type validated_data: dict
        :return: The created user instance.
        :rtype: django.contrib.auth.models.User
        """
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.

    This serializer handles the conversion between login data and their JSON representations.
    """
    username = serializers.CharField()
    password = serializers.CharField()

class GithubAuthSerializer(serializers.Serializer):
    access = serializers.CharField()
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.CharField()

class GithubReposSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    language = serializers.CharField(allow_null=True)
    repository_url = serializers.CharField()