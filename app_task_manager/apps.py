from django.apps import AppConfig


class AppTaskManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_task_manager'
    verbose_name = 'Task Manager'

    def ready(self):
        import app_task_manager.signals