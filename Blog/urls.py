# -*- coding: utf-8 -*-
__author__ = 'Евгений'

#coding: utf-8
from django.conf.urls import patterns, url

from Blog.views import PostsListView, PostDetailView

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/
                                               # будет выводиться список постов
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/
                                              # будет выводиться пост с определенным номером

)