from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class BaseViewSet(viewsets.ModelViewSet):
    """
    Base view set
    """
    pass


class AuthenticatedViewSet(BaseViewSet):
    """
    For authenticated views inherit from this class
    """
    permission_classes = (IsAuthenticated,)
