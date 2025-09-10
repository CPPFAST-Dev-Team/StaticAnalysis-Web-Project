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
    Represents a vulnerability found in a project.

    :param project: The project associated with this vulnerability.
    :type project: Project
    :param name: The name of the vulnerability.
    :type name: str
    :param file_location: The file location where the vulnerability was found.
    :type file_location: str
    :param line: The line number where the vulnerability was found.
    :type line: int
    :param vuln_id: The unique identifier for the vulnerability.
    :type vuln_id: str
    :param severity: The severity of the vulnerability. Must be one of 'LOW', 'MEDIUM', or 'SEVERE'.
    :type severity: str
    :param summary: A brief summary of the vulnerability.
    :type summary: str
    :param confidence: The confidence level of the vulnerability detection.
    :type confidence: Decimal
    """
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name="vulnerabilities")
    name = models.CharField(max_length=30)
    file_location = models.CharField(max_length=30)
    line = models.BigIntegerField()
    vuln_id = models.CharField(max_length=30)
    severity = models.CharField(max_length=30)  # Expected values: 'LOW', 'MEDIUM', 'SEVERE'
    summary = models.CharField(max_length=200)
    confidence = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.severity})"