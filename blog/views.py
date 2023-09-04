# If you're not using django channels
import requests
from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Subscriber, Tag
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
        post = Post.objects.get(slug=slug)
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


@api_view(['POST'])
def subscribe(request):
    email = request.data.get('email')

    if Subscriber.objects.filter(email=email).exists():
        return Response({'status': 'error', 'message': 'Email already exists in our database.'})

    subscriber = Subscriber(email=email)
    subscriber.save()
    return Response({'status': 'success', 'message': 'Thank you for subscribing to our newsletter!'})


class RelatedPostsView(APIView):
    def get(self, request, format=None):
        slug = self.request.query_params.get('slug')
        # Get the current post
        current_post = get_object_or_404(Post, slug=slug)

        # Get related posts using tags as the criteria
        related_posts = Post.objects.filter(
            tags__in=current_post.tags.all()).exclude(slug=slug)[:5]

        # Serialize the related posts
        serialized_posts = PostListSerializer(related_posts, many=True)

        return Response(serialized_posts.data)
