from rest_framework import serializers

from .models import Work, Collection

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'title', 'image_cdn_url', 'collection_title', 'image', 'user']

    collection_title = serializers.CharField(write_only=True)
    image = serializers.CharField(write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        collection, _created = Collection.objects.get_or_create(
            title=validated_data['collection_title'],
            user=validated_data['user']
        )

        work = Work(
            title=validated_data['title'],
            image=validated_data['image'],
            user=validated_data['user'],
            collection=collection
        )
        work.collection = collection
        work.save()
        return work

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'description', 'works']

    works = WorkSerializer(many=True, read_only=True)
