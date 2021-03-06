from datetime import date
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from galleria.settings import AWS_STORAGE_BUCKET_NAME,AWS_LOCATION
from urllib.parse import urlparse


class Collection(models.Model):
    title = models.CharField(max_length=244)
    date = models.DateField(default=date.today)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title if self.title is not None else 'Untitled Collection'

class Work(models.Model):
    title = models.CharField(max_length=244, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='works')
    collection = models.ForeignKey(Collection, null=True, blank=True, related_name='works', on_delete=models.CASCADE)

    def __str__(self):
        return self.title if self.title is not None else 'Untitled Work'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def image_cdn_url(self):
        if is_absolute(self.image.name):
            return self.image.name
        else:
            return f'https://{AWS_STORAGE_BUCKET_NAME}/{AWS_LOCATION}{self.image.name}'

    def get_collection_absolute_url(self):
        return settings.DOMAIN + reverse('works_collection', args=(self.collection.pk,))

    def image_tag(self):
        return mark_safe(f'<div class="works-admin-collection__image"><img alt="" src="{self.image_cdn_url()}" /></div>')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def image_tag_sm(self):
        return mark_safe(f'<div class="works-admin-collection__image works-admin-collection__image--small"><img alt="" src="{self.image_cdn_url()}" /></div>')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


def is_absolute(url):
    return bool(urlparse(url).netloc)
