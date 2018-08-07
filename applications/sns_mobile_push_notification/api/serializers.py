from common.base_serializers import BaseSerializer
from ..models import Device


class DeviceSerializer(BaseSerializer):

    class Meta:
        model = Device
        fields = ('token', 'os')
