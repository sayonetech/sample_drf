from ..models import Device
from .serializers import DeviceSerializer
from common.base_viewsets import AuthenticatedViewSet


# References
# https://github.com/intelligems/django-mobile-app/blob/master/core/mobile_devices/tasks.py
# https://github.com/jazzband/django-push-notifications
# https://github.com/fuzz-productions/django-sns-mobile-push-notification/

class DeviceViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows device to be registered or deleted
    This API support only for authenticated users
    """
    lookup_field = 'token'
    http_method_names = ['post', 'delete', 'put']
    serializer_class = DeviceSerializer
    queryset = Device.get_active_devices()

    def perform_create(self, serializer):
        device = serializer.save(user=self.request.user)
        #  For performance run this as an asynchronous task
        device.register()

    def perform_update(self, serializer):
        device = serializer.save()
        #  For performance run this as an asynchronous task
        device.refresh()

    def perform_destroy(self, instance):
        #  For performance run this as an asynchronous task
        instance.deregister()  # We are not deleting the device instead changing active=False


