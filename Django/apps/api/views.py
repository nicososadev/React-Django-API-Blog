from rest_framework import generics
from apps.blog.models import Blog
from .serializers import BlogSerializer

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.publishedBlogs.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
