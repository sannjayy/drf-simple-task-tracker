from .utils import Util

# Email Templates
new_task_message_template = "Hi {}, {} has just posted a new task - {}, Description:{}"


def new_task_email_notification(instance):
    print(instance)
    team_leader = instance.team.leader
    user = instance.created_by
    print(team_leader)
    print(user)
    email_data = {
        'to_email': 'znasofficial@gmail.com',
        'email_subject' : f'New Task Posted on Team: {instance.team.name}',
        
        'context': {
            'message': new_task_message_template.format(team_leader.full_name, user.full_name, instance.title, instance.description),
        }
        
    } 
    Util.send_mail(email_data, template_name='email/email_notification.html')
    return True