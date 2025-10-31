from rest_framework import viewsets
from .models import Job, Internship, SkillAssessment
from .serializers import JobSerializer, InternshipSerializer, SkillAssessmentSerializer
from rest_framework.permissions import IsAuthenticated

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

class InternshipViewSet(viewsets.ModelViewSet):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [IsAuthenticated]

class SkillAssessmentViewSet(viewsets.ModelViewSet):
    queryset = SkillAssessment.objects.all()
    serializer_class = SkillAssessmentSerializer
    permission_classes = [IsAuthenticated]
