from django.conf.urls import url
from .views import (CommentListAPIView,
                    CommentDetailAPIView)

# This is For check
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="thread"),
    url(r'^$', CommentListAPIView.as_view(), name="list"),
]
