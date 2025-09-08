from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
    
    def to_internal_value(self, data):
        title = data.get('title')
        if not title:
            raise serializers.ValidationError({'title': 'This field is required.'})

        tag, created = Tag.objects.get_or_create(title=title)
        return tag

class SnippetListSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name='snippet_detail',
        lookup_field='pk'
    )

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'note', 'tag', 'created_at', 'updated_at']


class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'tag', 'created_at', 'updated_at']

    def create(self, validated_data):
        tag = validated_data.pop('tag')
        return Snippet.objects.create(tag=tag, **validated_data)
    
    def update(self, instance, validated_data): 
        tag = validated_data.pop('tag', None)
        if tag:
            instance.tag = tag
        instance.title = validated_data.get('title', instance.title)
        instance.note = validated_data.get('note', instance.note)
        instance.save()
        return instance