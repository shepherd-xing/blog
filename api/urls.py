from django.conf.urls import url
from .views import PostListView, PostDetailView

urlpatterns = [
    url(r'^posts/$', PostListView.as_view(), name='post_list'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail')
]