from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news\/*$', views.news_show, name='news_show'),
    url(r'^videos\/*$', views.videos_show, name='videos_show'),
    url(r'^collections\/*$', views.collections_list, name='collections_list'),
    url(r'^collections\/(?P<collection>[a-z0-9\-]+)\/*$', views.collection, name='collection'),
    url(r'^collections\/(?P<collection>[a-z0-9\-]+)\/objects\/photos\/*$', views.object_photos, name='object_photos'),
    url(r'^collections\/(?P<collection>[a-z0-9\-]+)\/objects\/list\/*$', views.object_list, name='object_list'),
    url(r'^collections\/(?P<collection>[a-z0-9\-]+)\/objects\/category\/*$', views.object_cats, name='object_cats'),
    url(r'^collections\/(?P<collection>[a-z0-9\-]+)\/objects\/category\/(?P<category>[a-z0-9\-]+)\/*$', views.object_category, name='object_category'),
    url(r'^collections\/(?P<collection>[a-z0-9\-]+)\/objects\/(?P<object>[a-z0-9\-]+)\/*$', views.object, name='object'),
    url(r'^collections\/(?P<collection>[a-z0-9\-]+)\/tours$', views.tours, name='tours'),
    url(r'^forceupdate$', views.update_data, name='force_update')
]
