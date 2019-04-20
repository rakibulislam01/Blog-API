from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     RetrieveAPIView)
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly)
from blogApp.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PosCreateUpdateSerializer
from .permissions import IsOwnerReadonly


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PosCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerReadonly]

    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    #     instance = serializer.save()
    #     # send_email_confirmation(user=self.request.user, modified=instance)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        # queryset_list = super(PostListAPIView, super).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
                ).distinct()
        return queryset_list
