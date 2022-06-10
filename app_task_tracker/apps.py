from django.apps import AppConfig


class AppTaskManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_task_tracker'
    verbose_name = 'Task Tracker'

    def ready(self):
        import app_task_tracker.signals