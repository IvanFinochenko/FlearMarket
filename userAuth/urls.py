from django.conf.urls import url, include
from django.contrib import admin
from userAuth.views import *

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
]
