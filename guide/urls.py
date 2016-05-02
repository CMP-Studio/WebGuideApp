from django.conf.urls import url

urlpatterns = [
    url(r'^$', guide.views.main.index, name='index'),
    url(r'^forceupdate$', guide.views.main.update_data, name='force_update')
]
