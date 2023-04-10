from rest_framework import serializers

from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Tag
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = ["title", "slug", "summary", "date", "tags", "image"]


class PostSerializer(serializers.ModelSerializer):

   
    class Meta: 
        model = Post
        fields = "__all__"