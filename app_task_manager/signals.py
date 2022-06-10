from django.utils import timezone

# api_obj.update(count=api_key_data.count + 1, last_used=timezone.localtime(timezone.now())) 

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Team, Task

@receiver(post_save, sender=Task)
def perform_task_update_signal(sender, instance, created, **kwargs):

    if not created:

        current_date_time = timezone.localtime(timezone.now())
        if instance.status == 'done':
            Task.objects.filter(pk=instance.pk).update(completed_at=current_date_time)

        if instance.status == 'under process':
            Task.objects.filter(pk=instance.pk).update(started_at=current_date_time)
    
    