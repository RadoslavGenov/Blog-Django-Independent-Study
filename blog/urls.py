from django.conf.urls import url
from .feeds import LatestPostsFeed
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.PostListView.as_view(), name='post_list'), #with class based view
    
    #/blog/
    url(r'^$', views.post_list, name='post_list'),               #this is with view function
    
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
    
    #blog/search
    url(r'^search/$', views.post_search, name='post_search'),
    
    #blog/register
    url(r'^register/$', views.register, name='register'),


    url(r'^post/(?P<author>[-\w]+)/$', views.post, name='post'),

    ]