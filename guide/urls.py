from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.main.index, name='index'),
    url(r'^forceupdate$', views.main.update_data, name='force_update')
]
