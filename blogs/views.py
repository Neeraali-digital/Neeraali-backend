from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(status='published').order_by('-created_at')
    serializer_class = BlogSerializer
