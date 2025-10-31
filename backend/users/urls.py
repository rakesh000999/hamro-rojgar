from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentProfileViewSet, EmployerProfileViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentProfileViewSet)
router.register('employers', EmployerProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
