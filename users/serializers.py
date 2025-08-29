from django.contrib.auth.models import User
from rest_framework import serializers
from posts.serializers import PostListSerializer

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserDetailSerializer(serializers.ModelSerializer):
    posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'posts']

