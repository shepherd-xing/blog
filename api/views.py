from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.serializers import PostSerializer
from blog.models import Post

# Create your views here.
class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer