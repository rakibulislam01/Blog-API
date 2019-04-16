from django.conf.urls import url
from . import views

# This is For check
urlpatterns = [
    url('create/', views.post_create, name="create"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name="detail"),
    url('postlist/', views.post_list, name="list"),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete),
    # path('jango', views.index, name='jango'),
]
