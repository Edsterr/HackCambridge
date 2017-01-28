from django.conf.urls import url, include
from server.views import *
from server import views


urlpatterns = [
    url(r'^index/$', views.base.index, name="index"),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.base.profile, name="profile"),

    url(r'^productivity/add_record/$', views.productivity.addProductivityRecord, name="productivity_add_record"),


    url(r'^login/$', views.registration.user_login, name="user_login"),
    url(r'^register/$', views.registration.user_register, name="register"),
    url(r'^logout/$', views.registration.user_logout, name="user_logout")
]
