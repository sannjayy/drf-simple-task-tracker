from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet


app_name = 'task_tracker'

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='team')

urlpatterns = [

]+ router.urls