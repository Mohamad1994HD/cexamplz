from rest_framework import generics, permissions

from .serializers import PostDetailSerializer, PostListSerializer
from .models import Post

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    
