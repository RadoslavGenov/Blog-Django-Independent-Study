from django.conf.urls import url
from .feeds import LatestPostsFeed
from . import views

urlpatterns = [
    #post views
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    
    #/blog/tag/jazz
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    
    #/blog/2017/01/29/what-is-django
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', 
        views.post_detail,
        name='post_detail'),

    #/blog/1/share
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),

    #blog/feed
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),


    url(r'^post/$', views.post, name='post'),

    ]