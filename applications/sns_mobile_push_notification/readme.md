## Requirements
- boto3

## Usage
```
from sns_mobile_push_notification.models import Device
from sns_mobile_push_notification.tasks import register_device, refresh_device, send_sns_mobile_push_notification_to_device, deregister_device

# Given a valid token from Google's FCM(GCM), or Apple's APNs, create a device object.
device = Device()
device.token = "123456"
device.os = Device.IOS_OS
device.save()

# By registering a device, the token will be sent to SNS and SNS will return an ARN key which will be saved in the device object.
# ARN is required to send future push notification to SNS, regardless of the device type.
register_device(device)
device.refresh_from_db()
print(device.arn)

# You can refresh the device to make sure it is enabled and ready to use.
refresh_device(device)

# Now you can send the push notification to the the registered device.
if device.active and device.arn:
    send_sns_mobile_push_notification_to_device(
        device=device,
        notification_type="type",
        text="text",
        data={"a": "b"},
        title="title"
    )

# remove a device from SNS.
deregister_device(device)
```