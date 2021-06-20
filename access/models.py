from shortuuidfield import ShortUUIDField
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from works.models import Collection

class AccessToken(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.CharField(blank=True, null=True, max_length=255)
    expires = models.DateTimeField(blank=True, null=True)
    collection = models.OneToOneField(Collection, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    allow_children = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def get_share_url(self):
        return settings.DOMAIN + reverse('works_access_collection', args=(self.id,))
