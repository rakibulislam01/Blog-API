from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
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
from blogApp.api.permissions import IsOwnerReadonly
from blogApp.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from comments.models import Comment
from .serializers import (CommentSerializer,
                          CommentChildSerializer,
                          CommentListSerializer,
                          CommentDetailSerializer,
                          create_comment_serializer,)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get('type')
        slug = self.request.GET.get('slug')
        parent_id = self.request.GET.get('parent_id', None)
        return create_comment_serializer(model_type=model_type, slug=slug, parent_id=parent_id, user=self.request.user)


class CommentDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=8)
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerReadonly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagination_class = PostPageNumberPagination  # PostLimitOffsetPagination  # PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.filter(id__gte=0)
        # queryset_list = super(PostListAPIView, super).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list
