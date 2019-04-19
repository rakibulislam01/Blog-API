from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView)
from blogApp.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PosCreateUpdateSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PosCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PosCreateUpdateSerializer

    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'

    def perform_update(self, serializer):
        instance = serializer.save()
        # send_email_confirmation(user=self.request.user, modified=instance)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
