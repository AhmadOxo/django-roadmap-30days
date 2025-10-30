from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwner

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.IsAuthenticatedOrReadOnly()]