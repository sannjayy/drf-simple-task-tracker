
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

@receiver(post_save, sender=User)
def add_default_group(sender, instance, created, **kwargs):
    if not created:
        return      

    # Grouping Registered Users 
    if instance.is_superuser and instance.is_staff:
        group, create = Group.objects.get_or_create(name='Super Admin')
    else:
        print(instance.role)
        if instance.role == 'leader':
            role = 'Team Leader'

        elif instance.role == 'member':
            role = 'Team Member'

        elif instance.role == 'user':
            role = 'User'

        group, create = Group.objects.get_or_create(name=role)    


    instance.groups.add(group)
    instance.is_staff = True # Cause our all users can login to our admin panel.
    instance.save() 