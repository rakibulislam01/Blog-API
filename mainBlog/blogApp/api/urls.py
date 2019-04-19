from django.conf.urls import url
from . import views

# This is For check
urlpatterns = [
    url('list/', views.PostListAPIView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', views.PostDetailAPIView.as_view(), name="detail"),
    # url('postlist/', views.post_list, name="list"),
    # url(r'^(?P<id>\d+)/edit/$', views.post_update, name="update"),
    # url(r'^(?P<id>\d+)/delete/$', views.post_delete),
    # # path('jango', views.index, name='jango'),
]
