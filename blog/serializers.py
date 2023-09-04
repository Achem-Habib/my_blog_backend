from rest_framework import serializers

from .models import Post, Subscriber, Tag


class TagSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ["title", "slug", "image", "summary", "date", "tags",]


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ["title", "slug", "image", "summary",
                  "date", "table_of_contents", "body", "tags"]
