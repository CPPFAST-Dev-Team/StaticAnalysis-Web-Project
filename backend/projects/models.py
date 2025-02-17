from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    Represents a software project.

    :param owner: The user who owns the project.
    :type owner: User
    :param name: The name of the project.
    :type name: str
    :param description: A brief description of the project.
    :type description: str
    :param repository_url: The URL of the project's version control repository.
    :type repository_url: str
    :param created_at: The creation date and time of the project.
    :type created_at: datetime.datetime
    :param updated_at: The date and time when the project was last updated.
    :type updated_at: datetime.datetime
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_projects")
    users = models.ManyToManyField(User, related_name="projects")
    name = models.CharField(max_length=100)
    description = models.TextField()
    repository_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the Project.

        :return: The name of the project.
        :rtype: str
        """
        return self.name

class Vulnerability(models.Model):
    """
    Represents a security vulnerability found in a project.

    :param project: The project associated with this vulnerability.
    :type project: Project
    :param vuln_code: A unique code identifier for the vulnerability.
    :type vuln_code: str
    :param description: A detailed description of the vulnerability.
    :type description: str
    :param severity: The severity level of the vulnerability.
                     This could be values like "Low", "Medium", "High", etc.
    :type severity: str
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="vulnerabilities")
    vuln_code = models.CharField(max_length=50)
    description = models.TextField()
    severity = models.CharField(max_length=20)

    def __str__(self):
        """
        Returns a string representation of the Vulnerability.

        :return: A formatted string showing the vulnerability code and its severity level.
        :rtype: str
        """
        return f"{self.vuln_code} ({self.severity})"