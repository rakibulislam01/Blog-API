from django.conf.urls import url
from .views import (CommentCreateAPIView,
                    CommentListAPIView,
                    CommentDetailAPIView,
                    CommentEditAPIView)

# This is For check
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="thread"),
    url(r'^(?P<pk>\d+)/edit/$', CommentEditAPIView.as_view(), name="edit"),
    url(r'^$', CommentListAPIView.as_view(), name="list"),
    url(r'^create_comment/$', CommentCreateAPIView.as_view(), name="create_comment"),
]
