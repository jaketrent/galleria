from django.contrib import admin
from .models import AccessToken

@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    readonly_fields = ('get_share_url',)
