from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView)
from blogApp.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PosCreateUpdateSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PosCreateUpdateSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PosCreateUpdateSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
