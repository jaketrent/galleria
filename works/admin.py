from django.contrib.auth.models import User
from django.contrib import admin
from .models import Work, Collection

class WorkInline(admin.TabularInline):
    model = Work
    readonly_fields = ('title', 'date_created', 'image', 'description', 'user')
    extra = 0

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    inlines = [WorkInline]

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    # exclude = ['user',]

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

