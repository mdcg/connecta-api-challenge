from rest_framework import serializers

from api.models import Post
from api.serializers.users_serializers import UserInfoSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('user',)


class PostListSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        model = Post
        fields = '__all__'
