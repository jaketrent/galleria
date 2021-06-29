from access.models import AccessToken
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Work, Collection

class AccessTokenInline(admin.StackedInline):
    model = AccessToken
    # readonly_fields = ('title', 'date_created', 'image', 'description', 'user')
    # extra = 0

class WorkInline(admin.TabularInline):
    model = Work
    fields=('title', 'image_tag_sm', 'description',)
    readonly_fields = ('title', 'date_created', 'image', 'image_tag_sm', 'description', 'user')
    extra = 0

    class Media:
        css = {
            'all': ('works/admin.css',)
        }

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    inlines = [AccessTokenInline, WorkInline]

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    exclude = ['image_tag',]

    readonly_fields = ('image_tag',)

    class Media:
        css = {
            'all': ('works/admin.css',)
        }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = User.objects.filter(username=request.user.username)
        return super(WorkAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_readonly_fields(self, request, obj=None):
    #     if obj is not None:
    #         return self.readonly_fields + ('user',)
    #     return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['author'] = request.user
        request.GET = data
        return super(WorkAdmin, self).add_view(request, form_url="", extra_context=extra_context)

