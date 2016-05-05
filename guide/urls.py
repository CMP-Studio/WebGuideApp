from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news$', views.news_show, name='news_show'),
    url(r'^videos$', views.videos_show, name='videos_show'),
    url(r'^collections$', views.collections_list, name='collections_list'),
    url(r'^collections/(?P<slug>[a-z0-9\-]+)$', views.collection, name='collection'),
    url(r'^forceupdate$', views.update_data, name='force_update')
]
