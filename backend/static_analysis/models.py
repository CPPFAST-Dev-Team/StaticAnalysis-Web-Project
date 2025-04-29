from django.db import models

class AnalysisResult(models.Model):
    """
    Represents the result of a static code analysis run for a project.

    :param project: The project for which the analysis was run.
    :type project: Project
    :param timestamp: The date and time when the analysis was created.
    :type timestamp: datetime.datetime
    :param status: The current status of the analysis.
                   Choices are "PENDING", "IN_PROGRESS", "COMPLETED", and "FAILED".
    :type status: str
    :param result: The SARIF JSON result returned from the scanner.
    :type result: dict or None
    """
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name="analysis_results")
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

        :return: A summary including the project name and the analysis timestamp.
        :rtype: str
        """
        return f"Analysis for {self.project.name} at {self.timestamp}"