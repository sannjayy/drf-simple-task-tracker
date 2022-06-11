from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.text import slugify

# Create your models here.

USER_ROLE_OPTIONS = (
    ('user', 'User'),
    ('leader', 'Team Leader'),
    ('member', 'Team Member'),
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)

    role = models.CharField(choices=USER_ROLE_OPTIONS, max_length=25, default='user') # Can be multiple

    class Meta:
        verbose_name = 'User Account'        

    def save(self, *args, **kwargs):
        if not self.username:      
            """ 
                Generating Username by User's Email ID
            """      
            username = self.email.split('@')[0] if self.email else slugify(self.full_name[:6]).replace('-','_')
            counter = 1
            while User.objects.filter(username=username):
                username = username + str(counter)
                counter += 1
            self.username = username
        super().save(*args, **kwargs)


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}' if self.first_name else self.email

    # @property
    # def is_user(self):
    #     return self.user_type == 'user'
    
    # @property
    # def is_leader(self):
    #     return self.user_type == 'leader'
    
    # @property
    # def is_member(self):
    #     return self.user_type == 'leader'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }