from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Collection(models.Model):
    title = models.CharField(max_length=244)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=244, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collections = models.ManyToManyField(Collection, blank=True)
    image = models.ImageField(upload_to='works')

    def __str__(self):
        return self.title

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def image_cdn_url(self):
        return f'https://{AWS_STORAGE_BUCKET_NAME}/{AWS_LOCATION}{self.image.name}'
