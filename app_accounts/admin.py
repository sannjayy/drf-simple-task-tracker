from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.


# User Admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # List admin
    list_display = ('username', 'email', 'full_name', 'is_email_verified', 'is_active', 'role', 'date_joined')
    list_filter = ('role', 'is_email_verified', 'is_active', 'is_superuser')
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('User Credentials', {'fields': ('email', 'is_email_verified', 'username', 'password')}),        
        
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'groups')}), # 'user_permissions', 'groups'
    )
    # Creating new user from admin
    add_fieldsets = (
        ('User Information', {'classes': ('wide',), 'fields': ('email', 'password1', 'password2',)}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_superuser')}),
        
    )
    search_fields = ('email', 'first_name', 'last_name','username')
    ordering = ('-date_joined',)
    filter_horizontal = ('groups',)
    list_per_page = 10

    def get_queryset(self, request): 
        qs = super().get_queryset(request) 
        if not request.user.is_superuser:
            return qs.filter(username=request.user.username)
        return qs