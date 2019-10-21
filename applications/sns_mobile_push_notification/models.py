from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from common.base_models import AbstractBaseModel
from .client import Client


class Device(AbstractBaseModel):
    """
    Django model class representing a device.
    """

    # Constants
    IOS_OS = 'ios'
    ANDROID_OS = 'android'
    OS_CHOICES = (
        (IOS_OS, 'IOS'),
        (ANDROID_OS, 'Android'),
    )

    os = models.CharField(choices=OS_CHOICES, max_length=8)
    token = models.CharField(max_length=255, unique=True)
    arn = models.CharField(max_length=255, unique=True, blank=True, null=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name="user_devices",
        on_delete=models.CASCADE, null=True, blank=True)  # Can create device without user

    # Methods
    def __str__(self):
        """
        :return: string representation of this class.
        """
        return '%s device' % self.os_name

    # Metadata
    class Meta:
        ordering = ['-id']

    # Properties
    @property
    def is_android(self):
        return self.os == Device.ANDROID_OS

    @property
    def is_ios(self):
        return self.os == Device.IOS_OS

    @property
    def os_name(self):
        if self.is_android:
            return "ANDROID"
        elif self.is_ios:
            return "IOS"
        else:
            return "unknown"

    @staticmethod
    def get_active_devices():
        return Device.objects.filter(active=True)

    def register(self):
        """
        Method that registered a device on SNS for the first time,
        so that the device can receive mobile push notifications.
        it retrieves the endpoints ARN code and stores it.
        the ARN code will be used as the identifier for the device to send out mobile push notifications.
        :return: response from SNS
        """
        client = Client()
        if self.is_android:
            response = client.create_android_platform_endpoint(self.token)
        elif self.is_ios:
            response = client.create_ios_platform_endpoint(self.token)
        self.arn = response['EndpointArn']
        self.save(update_fields=['arn'])
        return response

    def refresh(self):
        """
        Method that checks/fixes the SNS endpoint corresponding a self.
        If the endpoint is deleted, disabled, or the it's token does not match the device token,
        it tries to recreate it.
        This task should be called upon a device update.
        :return: attributes retrieved from SNS
        """
        client = Client()
        try:
            attributes = client.retrieve_platform_endpoint_attributs(self.arn)
            endpoint_enabled = (attributes['Enabled'] == True) or (attributes['Enabled'].lower() == "true")
            tokens_matched = attributes['Token'] == self.token
            if not (endpoint_enabled and tokens_matched):
                client.delete_platform_endpoint(self.arn)
                self.register()
                attributes = client.retrieve_platform_endpoint_attributs(self.arn)
            return attributes
        except Exception as e:
            if 'Endpoint does not exist' in str(e):
                self.register()
                attributes = client.retrieve_platform_endpoint_attributs(self.arn)
                return attributes
            else:
                self.active = False
                self.save(update_fields=['active'])

    def deregister(self):
        """
        Method that deletes registered a device from SNS.
        :return: none
        """
        client = Client()
        client.delete_platform_endpoint(self.arn)
        self.active = False
        self.save(update_fields=['active'])

    def send(self, notification_type, text, data, title):
        """
        Method that sends out a mobile push notification to a specific self.
        :param notification_type: type of notification to be sent
        :param text: text to be included in the push notification
        :param data: data to be included in the push notification
        :param title: title to be included in the push notification
        :return: response from SNS
        """
        log = Log(
            device=self,
            notification_type=notification_type,
        )
        log.save()

        client = Client()
        params = {
            'arn': self.arn,
            'text': text,
            'title': title,
            'notification_type': notification_type,
            'data': data,
            'id': log.id,
        }
            

        if self.is_android:
            message, response = client.publish_to_android(**params)
        elif self.is_ios:
            message, response = client.publish_to_ios(**params)

        log.message = message
        log.response = response
        log.save()

        return response


class Log(AbstractBaseModel):
    """
    Django model class representing a notification log.
    """
    device = models.ForeignKey('Device', on_delete=models.CASCADE, related_name='notification_logs', null=True, blank=True)
    notification_type = models.CharField(max_length=255, null=True, blank=True)
    arn = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)

    # Methods
    def __str__(self):
        """
        :return: string representation of this class.
        """
        return '"%s" notification log for - "%s"' % (self.notification_type, self.device)
