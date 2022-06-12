from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import Team, Task
from .permissions import IsOwnerOfObject
from .paginations import TeamResultsPagination, TaskResultsPagination
from .serializers import TeamSerializer, TaskSerializer
# Create your views here.

# TEAM VIEWSET
class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    lookup_field = 'slug'
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['^name', 'slug']
    ordering = ('-created_at', '-id',)
    throttle_classes = [UserRateThrottle]
    pagination_class = TeamResultsPagination
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        current_user = self.request.user
        return Team.objects.filter(Q(created_by=current_user) | Q(leader=current_user) | Q(members__in=[current_user])).distinct()
    
    def destroy(self, request, *args, **kwargs):
        current_user = request.user 
        instance = self.get_object()
        
        if current_user.role != 'user':
            return response.Response({'error':'You dont have the permission to delete.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if instance.created_by != current_user:
            return response.Response({'error':'You are not the owner of this team.'}, status=status.HTTP_400_BAD_REQUEST)

        return super(TeamViewSet, self).destroy(request, *args, **kwargs)

    

# TASK VIEWSET

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    lookup_field = 'slug'
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['^name','^description', 'slug']
    ordering = ('-created_at', '-id', '-status', '-priority')
    filterset_fields = ('priority', 'status')
    throttle_classes = [UserRateThrottle]
    pagination_class = TaskResultsPagination
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        current_user = self.request.user
        return Task.objects.filter(Q(created_by=current_user) | Q(assigned_to=current_user) | Q(team__leader=current_user) | Q(team__members__in=[current_user])).distinct()

        
    def destroy(self, request, *args, **kwargs):
        current_user = request.user 
        instance = self.get_object()
        
        if current_user.role != 'user':
            return response.Response({'error':'You dont have the permission to delete.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if instance.created_by != current_user:
            return response.Response({'error':'You are not the owner of this team.'}, status=status.HTTP_400_BAD_REQUEST)

        return super(TeamViewSet, self).destroy(request, *args, **kwargs)