from django.urls import path

from blog import views

urlpatterns = [
    path('post-list/', views.PostListView.as_view(), name="post-list"),
    path('post/', views.PostView.as_view(), name="post"),
    path('latest-posts/', views.LatestPostView.as_view(), name="latest-posts"),
    path('related-posts/', views.RelatedPostsView.as_view(), name="related-posts"),
    path('tags/', views.TagListView.as_view(), name="tag-list"),
    path("tag/<slug:slug>/", views.TagPostListAPIView.as_view(), name="tag-post-list"),
    path('subscribe/', views.subscribe, name="email-subscription"),

]
