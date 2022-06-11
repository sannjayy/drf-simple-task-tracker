from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, TaskViewSet


app_name = 'task_tracker'

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='team')
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = [

]+ router.urls