from django.db import models
from users.models import EmployerProfile, StudentProfile

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    skills_required = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Internship(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    skills_required = models.TextField(blank=True)
    duration_weeks = models.IntegerField(default=12)
    created_at = models.DateTimeField(auto_now_add=True)

class SkillAssessment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    score = models.IntegerField()
    max_score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)
