from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    
    @action(detail=False, methods=['get'])
    def published(self, request):
        """Get only published blogs for public display"""
        published_blogs = Blog.objects.filter(status='published').order_by('-created_at')
        serializer = self.get_serializer(published_blogs, many=True)
        return Response(serializer.data)
