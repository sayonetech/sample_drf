from django.contrib.auth import get_user_model

from rest_framework import serializers

from common.base_serializers import BaseSerializer
from ..models import Post


class PostUserSerializer(BaseSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'name')

    def get_name(self, user):
        return user.get_full_name()


class PostSerializer(BaseSerializer):
    user = PostUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('text', 'user', 'created')
