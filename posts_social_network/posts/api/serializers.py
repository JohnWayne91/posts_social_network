from django.contrib.auth import get_user_model

from rest_framework import serializers

from ..models import Post, Like

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'last_login')


class AnalyticSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ('created_at', 'total_likes')


class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField(required=False)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'body',
            'total_likes'
        )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'