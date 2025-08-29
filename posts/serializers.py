from rest_framework import serializers
from .models import Post, Comment, Tag
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author_name', 'body', 'created_at']
        read_only_fields = ['post', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'created_at', 'comment_count', 'tags']

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, required=False)
    author_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'author_id', 'created_at', 'updated_at', 'comments', 'tags']
        read_only_fields = ['created_at', 'updated_at', 'author']

    def get_author(self, obj):
        return {'id': obj.author.id, 'username': obj.author.username, 'email': obj.author.email}

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters.")
        return value

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            author = request.user
        else:
            author_id = validated_data.pop('author_id', None)
            if author_id:
                author = User.objects.get(pk=author_id)
            else:
                raise serializers.ValidationError("Author must be authenticated or author_id provided.")
        post = Post.objects.create(author=author, title=validated_data['title'], body=validated_data.get('body', ''))
       
        for t in tags_data:
            if isinstance(t, dict):
                name = t.get('name')
            else:
                name = t
            if not name:
                continue
            tag_obj, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag_obj)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        if tags_data is not None:
            instance.tags.clear()
            for t in tags_data:
                name = t.get('name') if isinstance(t, dict) else t
                if not name: continue
                tag_obj, _ = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag_obj)
        return instance
