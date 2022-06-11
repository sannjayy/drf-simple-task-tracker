from django.contrib import admin
from django.db.models import Q
from .models import Team, Task

# TEAM ADMIN VIEW
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'leader', 'status', 'created_by', 'created_at', 'updated_at']
    # fields = ['title', 'order', 'slug', 'is_menu', 'status']
    search_fields = ('name','slug', 'leader__first_name')
    list_filter = ('status', )
    readonly_fields = ('slug', 'created_by',)
    list_display_links = ('name', 'id')
    filter_horizontal = ('members',)
    autocomplete_fields = ('leader',)
    list_per_page = 10
    

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()

    def get_queryset(self, request): 
        qs = super().get_queryset(request) 
        if not request.user.is_superuser:
            current_user = request.user
            return qs.filter(Q(created_by=current_user) | Q(leader=current_user) | Q(members__in=[current_user]))
        return qs
    
    def has_add_permission(self, request, obj=None):       
        return request.user.role == 'user'

    def has_change_permission(self, request, obj=None):
        return any([request.user.role == 'user', request.user.role == 'leader'])

    def has_delete_permission(self, request, obj=None):
        return request.user.role == 'user'



# TASK ADMIN VIEW
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'title', 'priority', 'status',  'assigned_to','started_at', 'completed_at', 'created_by','created_at', 'updated_by', 'updated_at']
    search_fields = ('team__name','title', 'leader__first_name')
    list_filter = ('priority', 'status')
    readonly_fields = ('slug', 'created_by', 'updated_by', 'started_at', 'completed_at')
    autocomplete_fields = ('assigned_to', )
    list_display_links = ('title', 'id')
    list_per_page = 10
    fieldsets = (
        ('Task Info', {'fields': ('team', 'title', 'description')}),
        ('Actions', {'fields': ('priority', 'status', 'assigned_to')}),
    )

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()

    def get_queryset(self, request): 
        qs = super().get_queryset(request) 
        if not request.user.is_superuser:
            current_user = request.user
            return qs.filter(Q(created_by=current_user) | Q(assigned_to=current_user) | Q(team__leader=current_user) | Q(team__members__in=[current_user]))
        return qs
    
    # def has_add_permission(self, request, obj=None):       
    #     return any([request.user.role == 'user', request.user.role == 'leader'])

    # def has_change_permission(self, request, obj=None):
    #     return request.user.role == 'member'

    def has_delete_permission(self, request, obj=None):
        return request.user.role == 'user'