from django.conf.urls import url
from . import views

app_name = 'loginapp'

urlpatterns = [
    #<WebSite.com>
    url(r'^$', views.index, name="index"),
    #<WebSite.com>/home/
    url(r'^login/$', views.index, name="index"),
]
