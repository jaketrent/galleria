from django.urls import path
from .views import CollectionListView, CollectionView, WorkDetailView, AccessCollectionDetailView

urlpatterns = [
    path('', CollectionListView.as_view(), name='works_collections'),
    path('collection/<int:pk>', CollectionView.as_view(), name='works_collection'),
    path('work/<int:pk>', WorkDetailView.as_view(), name='works_work'),
    path('access/collection/<access_token>', AccessCollectionDetailView.as_view(), name='works_access_collection'),
]
