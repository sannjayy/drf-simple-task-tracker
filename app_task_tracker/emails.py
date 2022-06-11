from .utils import Util
from .tasks import send_async_email_task
# Email Templates
new_task_message_template = "Hi {}, {} has just posted a new task - {}, Description:{}"


def new_task_email_notification(instance):
    team_leader = instance.team.leader
    user = instance.created_by
    email_data = {
        'to_email': 'znasofficial@gmail.com',
        'email_subject' : f'New Task Posted on Team: {instance.team.name}',
        
        'context': {
            'message': new_task_message_template.format(team_leader.full_name, user.full_name, instance.title, instance.description),
        }
        
    } 
    # Util.send_mail(email_data, template_name='email/email_notification.html') # TODO: Uncomment If you wish to send emails using Threading
    send_async_email_task.delay(email_data, template_name='email/email_notification.html') # Celery Task
    return True