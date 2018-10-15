from ..models import Like
from .serializers import LikeSerializer
from common.base_viewsets import AuthenticatedViewSet



class LikeViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows Like instances
    to be listed or added or viewed.
    """
    http_method_names = ['get', 'post', ]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


