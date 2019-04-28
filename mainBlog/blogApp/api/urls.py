from django.conf.urls import url
from .views import (PostListAPIView,
                    PostCreateAPIView,
                    PostUpdateAPIView,
                    PostDeleteAPIView,
                    PostDetailAPIView)
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="list"),
    url(r'^create_post/$', PostCreateAPIView.as_view(), name="create_post"),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name="detail"),
    # url(r'^api/v1/some-resource$', csrf_exempt(SomeApiView.as_view())),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name="update"),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteAPIView.as_view(), name="delete"),
]
