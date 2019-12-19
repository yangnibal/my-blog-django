from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    id = serializers.CharField(read_only=True)
    post_key = serializers.CharField(read_only=True)
    posted_date = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ['author', 'post_title', 'post_content', 'post_key', 'post_thumbnail', 'id', 'posted_date']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    post = serializers.CharField(source='post.post_key')
    id = serializers.CharField(read_only=True)
    commented_date = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ['comment_message', 'author', 'post', 'id', 'commented_date']