from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news$', views.news_show, name='news_show'),
    url(r'^forceupdate$', views.update_data, name='force_update')
]
