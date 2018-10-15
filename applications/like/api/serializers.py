from django.contrib.auth import get_user_model
from rest_framework import serializers
from common.base_serializers import BaseSerializer
from ..models import Like
from rest_framework.validators import UniqueTogetherValidator
from django.utils.translation import ugettext_lazy as _



class LikeUserSerializer(BaseSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'name',)

    def get_name(self, user):
        return user.get_full_name()


class LikeSerializer(serializers.ModelSerializer):
    user = LikeUserSerializer(read_only=True, default=serializers.CurrentUserDefault())
    content_type_name = serializers.CharField(source="content_type.name", read_only=True)


    class Meta:
        model = Like
        fields = ('id', 'url', 'user', 'created', 'content_type_name', 'content_type', 'content_type_id', 'object_id', )

        validators = [UniqueTogetherValidator(
            queryset=Like.objects.all(),
            fields=('user', 'object_id', 'content_type'),
            message=_("Already liked")
        )]

    def validate(self, attrs):
        try:
            attrs['content_object'] = attrs['content_type'].model_class().objects.get(pk=attrs['object_id'])
        except:
            raise serializers.ValidationError(
                {'object_id': ['Invalid pk "' + str(attrs['object_id']) + '" - object does not exist.']})
        return attrs