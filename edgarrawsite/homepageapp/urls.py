from django.conf.urls import url
from . import views
urlpatterns = [
    #<WebSite.com>
    url(r'^$', views.index, name="index"),
    #<WebSite.com>/home/
    url(r'^home/$', views.index, name="index"),
]
