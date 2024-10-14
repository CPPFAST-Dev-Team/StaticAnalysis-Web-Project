from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    file_location =  models.CharField(max_length=30)
    line = models.BigIntegerField()
    vuln_id = models.CharField(max_length=30)
    severity = models.CharField(max_length=30)
    summary = models.CharField(max_length=200)
    confidence = models.DecimalField(max_digits=3, decimal_places=2)
