from django.views.generic import (
    ListView,
    DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Collection, Work

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
