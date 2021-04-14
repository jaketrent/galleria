from datetime import datetime
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import AccessMixin
from .models import AccessToken

class AccessTokenRequiredMixin(AccessMixin):
    """Verify that the token exists and is valid"""
    def dispatch(self, request, *args, **kwargs):
        access_token = kwargs['access_token']

        token = AccessToken.objects.filter(
            Q(id=access_token),
            Q(active=True),
            Q(expires__gte=datetime.today()) | Q(expires__isnull=True)
        ).first()

        if token is None:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

