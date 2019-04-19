from django.conf.urls import url
from .views import (PostListAPIView,
                    PostUpdateAPIView,
                    PostDeleteAPIView,
                    PostDetailAPIView)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name="delete"),
]
