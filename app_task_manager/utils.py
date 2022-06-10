import string, random, threading
from django.utils.text import slugify
from django.template.loader import render_to_string 
from django.core.mail import EmailMultiAlternatives

# Email Sending Thread
class EmailThread(threading.Thread):
    
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class Util:   
    @staticmethod
    def send_mail(data, template_name=None):
        html_version = template_name
        html_message = render_to_string(html_version, { 'context': data['context'], }).strip()   

        email = EmailMultiAlternatives(subject=data['email_subject'], body=html_message, to=[data['to_email']])
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'
        # email.send()

        EmailThread(email).start()



# -------------------------------------------------- #

#  Unique Slug Generator
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug = None):
    slug =  slugify(new_slug) if new_slug is not None else slugify(instance.title)

    Class = instance.__class__
    max_length = Class._meta.get_field('slug').max_length
    slug = slug[:max_length]
    if qs_exists := Class.objects.filter(slug=slug).exists():
        new_slug = "{slug}-{randstr}".format(
            slug = slug[:max_length-20], randstr = random_string_generator(size = 17))

        return unique_slug_generator(instance, new_slug = new_slug)
    return slug







