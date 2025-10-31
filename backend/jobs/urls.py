from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, InternshipViewSet, SkillAssessmentViewSet

router = DefaultRouter()
router.register('jobs', JobViewSet)
router.register('internships', InternshipViewSet)
router.register('assessments', SkillAssessmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
