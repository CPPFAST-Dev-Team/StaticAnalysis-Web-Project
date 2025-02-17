from django.db import models
from projects.models import Project

class AnalysisResult(models.Model):
    """
    Represents the result of a static code analysis for a project.

    :param project: The project associated with this analysis result.
    :type project: Project
    :param timestamp: The time when the analysis was performed.
    :type timestamp: datetime
    :param status: The current status of the analysis.
    :type status: str
    :param result: The detailed analysis result in JSON format.
    :type result: dict or None
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='analysis_results')
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('PENDING', 'Pending'),
            ('IN_PROGRESS', 'In Progress'),
            ('COMPLETED', 'Completed'),
            ('FAILED', 'Failed')
        ], 
        default='PENDING'
    )
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the AnalysisResult.

        :return: A string describing the analysis result.
        :rtype: str
        """
        return f"Analysis for {self.project.name} - {self.timestamp}"