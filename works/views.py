from django.urls.base import reverse
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from .models import Collection, Work
from access.views import AccessTokenRequiredMixin
from access.models import AccessToken
from access.forms import CreateAccessTokenForm
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import WorkSerializer, CollectionSerializer

class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    ordering = ['-date', '-date_created']

class CollectionDetailView(LoginRequiredMixin, DetailView):
    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        collection = self.get_object()
        context['form'] = CreateAccessTokenForm({ 'collection_id': collection.id })
        return context

class CreateAccessTokenFormView(SingleObjectMixin, FormView):
    template_name = 'works/collection_detail.html'
    form_class = CreateAccessTokenForm
    model = Collection

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateAccessTokenForm(request.POST)
        if form.is_valid():
            print(form.data['collection_id'])
            self.object.access_token = AccessToken.objects.create(collection_id=form.data['collection_id'], created_by=request.user)
            self.object.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('works_collection', kwargs={'pk': self.object.pk})

class CollectionView(View):
    def get(self, request, *args, **kwargs):
        view = CollectionDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreateAccessTokenFormView.as_view()
        return view(request, *args, **kwargs)

class WorkDetailView(LoginRequiredMixin, DetailView):
    model = Work

class AccessCollectionDetailView(AccessTokenRequiredMixin, TemplateView):
    model = Collection
    template_name = 'works/collection_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        access_token = kwargs['access_token']
        context['collection'] = AccessToken.objects.get(id=access_token).collection
        return context

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

