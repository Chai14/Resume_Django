from django.db import models

class resume_education(models.Model):
    school_name = models.CharField(max_length=50)
    school_duration = models.CharField(max_length=50)
    school_score = models.TextField()

class resume_projects(models.Model):
    project_name = models.CharField(max_length=50)
    project_duration = models.CharField(max_length=50)
    project_details = models.TextField()

class resume_certificates(models.Model):
    certi_name = models.CharField(max_length=50)
    certi_month = models.CharField(max_length=50)
    certi_details = models.TextField()

# Create your models here.
