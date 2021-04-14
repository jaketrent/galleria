from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Collection, Work
from access.views import AccessTokenRequiredMixin
from access.models import AccessToken

class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    # template_name = 'works/collections.html'
    # context_object_name = 'collections'
    ordering = ['-date_created']
    paginate_by = 10

class CollectionDetailView(LoginRequiredMixin, DetailView):
    model = Collection

class WorkDetailView(LoginRequiredMixin, DetailView):
    model = Work

class AccessCollectionDetailView(AccessTokenRequiredMixin, TemplateView):
    model = Collection
    template_name = 'works/collection_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        access_token = kwargs['access_token']
        context['collection'] = AccessToken.objects.filter(id=access_token).first().collection
        return context

