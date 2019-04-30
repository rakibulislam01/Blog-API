from django.db.models import Q
from django.contrib.auth import get_user_model
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

from .serializers import UserCreateSerializer

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


