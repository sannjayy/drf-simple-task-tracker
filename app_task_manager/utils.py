import string, random
from django.utils.text import slugify

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

