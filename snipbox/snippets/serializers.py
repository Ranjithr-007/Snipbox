from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'tag', 'created_at', 'updated_at']

    def create(self, validated_data):
        tag_data = validated_data.pop('tag')
        print(tag_data)
        tag, created= Tag.objects.get_or_create(title=tag_data['title'])
        return Snippet.objects.create(tag=tag, **validated_data)