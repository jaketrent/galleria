from django.views.generic import (
    ListView,
    DetailView
)
from .models import Collection, Work

class CollectionListView(ListView):
    model = Collection
    # template_name = 'works/collections.html'
    # context_object_name = 'collections'
    ordering = ['-date_created']
    paginate_by = 10

class CollectionDetailView(DetailView):
    model = Collection

class WorkDetailView(DetailView):
    model = Work
