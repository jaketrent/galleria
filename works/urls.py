from django.urls import path
from .views import CollectionListView, CollectionDetailView, WorkDetailView

urlpatterns = [
    path('', CollectionListView.as_view(), name='works_collections'),
    path('collection/<int:pk>', CollectionDetailView.as_view(), name='works_collection'),
    path('work/<int:pk>', WorkDetailView.as_view(), name='works_work'),
]
