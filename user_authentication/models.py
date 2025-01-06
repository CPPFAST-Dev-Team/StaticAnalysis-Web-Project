from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    """
    Represents additional user profile information.

    :param user: The user associated with this profile
    :type user: User
    :param bio: A brief biography of the user
    :type bio: str
    :param location: The user's location
    :type location: str
    :param birth_date: The user's birth date
    :type birth_date: date
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_auth_profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the UserProfile.

        :return: The username of the associated user
        :rtype: str
        """
        return self.user.username