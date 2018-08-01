from ..models import Post
from .serializers import PostSerializer
from common.base_viewsets import AuthenticatedViewSet


class PostViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows Post instances
    to be listed or added or viewed.
    """
    http_method_names = ['get', 'post',]
    queryset = Post.objects.public()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
