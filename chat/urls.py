from django.conf.urls import url

from chat import views

urlpatterns = [
    url(r'^(?P<chatroom_slug>[\w]+)/$', views.chatroom),
    url(r'^create/$', views.chatroom),
]
