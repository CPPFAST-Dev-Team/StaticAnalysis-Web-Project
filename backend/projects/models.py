from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    Represents a project in the system.

    This model stores information about projects, including their name, description,
    repository URL, owner, creation and update times, and associated users.

    :param name: The name of the project
    :type name: str
    :param description: A detailed description of the project
    :type description: str
    :param repository_url: The URL of the project's repository
    :type repository_url: str
    :param owner: The user who owns the project
    :type owner: User
    :param created_at: The date and time when the project was created
    :type created_at: datetime
    :param updated_at: The date and time when the project was last updated
    :type updated_at: datetime
    :param users: The users associated with this project
    :type users: ManyToManyField
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    repository_url = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        """
        Returns a string representation of the Project.

        :return: The name of the project
        :rtype: str
        """
        return self.name