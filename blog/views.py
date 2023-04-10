# If you're not using django channels
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Tag
from .serializers import PostListSerializer, PostSerializer, TagSerializer


class PostListView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(published=True)



class LatestPostView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('-date')[:10]
    

class PostView(APIView):

    def get(self, request, format=None):
        slug = self.request.query_params.get('slug')
        post = Post.objects.get(slug =slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    

class TagListView(ListAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.annotate(post_count=Count('post'))

class TagPostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        tag_slug = self.kwargs["slug"]
        return Post.objects.filter(tags__slug=tag_slug)