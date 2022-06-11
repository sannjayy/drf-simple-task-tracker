from django.http import HttpResponse
from celery import shared_task
from django.template.loader import render_to_string 
from django.core.mail import EmailMultiAlternatives

@shared_task
def send_async_email_task(data, template_name=None):
    print('Email Sending Task Initiated') # FIXME: Delete this line
    html_version = template_name
    html_message = render_to_string(html_version, { 'context': data['context'], }).strip()   

    email = EmailMultiAlternatives(subject=data['email_subject'], body=html_message, to=[data['to_email']])
    email.content_subtype = 'html'
    email.mixed_subtype = 'related'
    email.send()
