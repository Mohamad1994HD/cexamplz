from django.conf.urls import url

from .api import (
    PostListAPIView,
    PostDetailAPIView,
)
from .views import index

urlpatterns = [
    url(r'^api/v1/posts/(?P<pk>\d+)$',  PostDetailAPIView.as_view(), name='post'),
    url(r'^api/v1/posts$', PostListAPIView.as_view(), name='api_list'),
    url(r'^', index, name='index'),
] 
