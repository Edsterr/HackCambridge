from django.conf.urls import url, include
from django.contrib import admin
from server import views

urlpatterns = [
    url(r'^productivity/update', views.productivity.update, "productivity_update"),
]
