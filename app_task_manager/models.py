from django.db import models
from .utils import unique_slug_generator
from django.contrib.auth import get_user_model
User = get_user_model()

# TEAM MODEL

class Team(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    leader = models.ForeignKey(User, related_name='leader', limit_choices_to={'role': 'leader'}, on_delete=models.SET_NULL, null=True, verbose_name='Team leader')
    members = models.ManyToManyField(User, related_name='members', blank=True, limit_choices_to={'role': 'member'}, verbose_name='Team members')
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.status = True
            self.slug = unique_slug_generator(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# TASK MODEL 

PRIORITY_OPTIONS = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

STATUS_OPTIONS = (
    ('under review', 'Under Review'),
    ('assigned', 'Assigned'),
    ('in process', 'In Process'),
    ('done', 'Done'),
)

class Task(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    priority = models.CharField(max_length=25, choices=PRIORITY_OPTIONS, default='medium')
    status = models.CharField(max_length=25, choices=STATUS_OPTIONS, default='under review')

    assigned_to = models.ForeignKey(User, related_name='assigned_to', limit_choices_to={'role': 'member'}, on_delete=models.SET_NULL, blank=True, null=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='task_created_by', null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='task_updated_by', null=True, verbose_name='Last updated by')
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title