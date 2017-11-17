from rest_framework import serializers

from .models import Post

serializer_fields = [
    'id',
    'topic_name',
    'title',
    'timestamp',
    'difficulty',
]

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post    
        fields = serializer_fields + ['content']
        

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = serializer_fields 
