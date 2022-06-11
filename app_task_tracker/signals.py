from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Task
from .emails import new_task_email_notification

@receiver(post_save, sender=Task)
def perform_task_update_signal(sender, instance, created, **kwargs):

    if not created:
        current_date_time = timezone.localtime(timezone.now())
        task_obj = Task.objects.filter(pk=instance.pk)
        if instance.assigned_to:
            # TODO: Send a notification mail to assigned member
            task_obj.update(status='assigned')

        if instance.status == 'done':
            # TODO: Send a notification mail to user
            task_obj.update(completed_at=current_date_time)

        if instance.status == 'in process':
            task_obj.update(started_at=current_date_time)
    
    else:
        new_task_email_notification(instance) # if new created then sending mail to the team leader
    
    