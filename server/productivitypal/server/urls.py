from django.conf.urls import url, include
from server.views import *
from server import views


urlpatterns = [
    url(r'^index/', views.productivity.update, name="index"),
    url(r'^productivity/update/$', views.productivity.update, name="productivity_update"),

    url(r'^registration/login/$', views.registration.user_login, name="user_login"),
    url(r'^registration/register/$', views.registration.user_register, name="register"),
    url(r'^registration/logout/$', views.registration.user_logout, name="user_logout")
]
