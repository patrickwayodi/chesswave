from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    url(r'^$', views.home_page, name='home_page'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/(?P<player>[\w\d]+)/$', views.profile, name='profile'),
    url(r'^docs/$', views.docs, name='docs'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^accounts/register/$', views.register, name='register'),
    
    url(r'^game/list/$', views.game_list, name='game_list'),
    url(r'^game/list/(?P<player>[\w\d]+)/$', views.game_list_user, name='game_list_user'),    
    url(r'^game/(?P<pk>[0-9]+)/$', views.game_detail, name='game_detail'),    
    url(r'^game/new/(?P<white>[\w\d]+)/(?P<black>[\w\d]+)/$', views.game_new, name='game_new'),
    url(r'^game/(?P<pk>[0-9]+)/play/$', views.game_play, name='game_play'),
    url(r'^game_drafts/$', views.game_draft_list, name='game_draft_list'),
    url(r'^game/(?P<pk>[0-9]+)/publish/$', views.game_publish, name='game_publish'),
    url(r'^game/(?P<pk>[0-9]+)/remove/$', views.game_remove, name='game_remove'),             

    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'), 
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'), 
    
    url(r'^search/profile/$', views.search_profile, name='search_profile'),          
    url(r'^search/profile/(?P<player>[\w\d]+)/$', views.search_profile_results, name='search_profile_results'),              
]
