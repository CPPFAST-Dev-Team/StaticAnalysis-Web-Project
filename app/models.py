from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    Represents a project in the system.

    :param user: The user who owns the project
    :type user: User
    :param name: The name of the project
    :type name: str
    :param github_link: The GitHub link of the project
    :type github_link: str
    :param icon: The icon representing the project
    :type icon: str
    :param num_high_issues: The number of high-priority issues
    :type num_high_issues: int
    :param num_med_issues: The number of medium-priority issues
    :type num_med_issues: int
    :param num_low_issues: The number of low-priority issues
    :type num_low_issues: int
    :param token: The token associated with the project
    :type token: str
    :param team: The team associated with the project
    :type team: str
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    github_link = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    num_high_issues = models.BigIntegerField()
    num_med_issues = models.BigIntegerField()
    num_low_issues = models.BigIntegerField()
    token = models.CharField(max_length=30)
    team = models.CharField(max_length=30)

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

class AnalysisResult(models.Model):
    """
    Represents the result of a code analysis for a project.

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