from rest_framework import generics, permissions
from apps.blog.models import Blog
from .serializers import BlogSerializer

class UserBlogDetail(permissions.BasePermission):

    message = 'You do not have permissions to edit this Blog'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.author == request.user


class BlogList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Blog.publishedBlogs.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView, UserBlogDetail):
    permission_classes = [UserBlogDetail]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
