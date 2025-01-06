from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

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

class AnalysisResult(models.Model):
    """
    Represents the result of a static code analysis for a project.

    :param project: The project associated with this analysis result
    :type project: Project
    :param timestamp: The time when the analysis was performed
    :type timestamp: datetime
    :param status: The current status of the analysis
    :type status: str
    :param result: The detailed result of the analysis
    :type result: JSON
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='analysis_results')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed')
    ], default='PENDING')
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the AnalysisResult.

        :return: A string describing the analysis result
        :rtype: str
        """
        return f"Analysis for {self.project.name} - {self.timestamp}"

class Vulnerability(models.Model):
    """
    Represents a vulnerability found in a project.

    :param project: The project associated with this vulnerability
    :type project: Project
    :param name: The name of the vulnerability
    :type name: str
    :param file_location: The file location where the vulnerability was found
    :type file_location: str
    :param line: The line number where the vulnerability was found
    :type line: int
    :param vuln_id: The unique identifier for the vulnerability
    :type vuln_id: str
    :param severity: The severity level of the vulnerability
    :type severity: str
    :param summary: A brief summary of the vulnerability
    :type summary: str
    :param confidence: The confidence level of the vulnerability detection
    :type confidence: Decimal
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    file_location = models.CharField(max_length=30)
    line = models.BigIntegerField()
    vuln_id = models.CharField(max_length=30)
    severity = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    confidence = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        """
        Returns a string representation of the Vulnerability.

        :return: A string describing the vulnerability
        :rtype: str
        """
        return f"{self.name} ({self.severity})"