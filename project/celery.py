import os
from django.conf import settings
from celery import Celery

# default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asis/Kolkata')
app.config_from_object(settings, namespace='CELERY')


app.autodiscover_tasks()