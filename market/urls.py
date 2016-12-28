from django.conf.urls import url, include
from market.views import *


urlpatterns = [
    url(r'^additem/', addItem, name='addItem'),
    url(r'^search/', search, name='search'),
    url(r'^offer/', offer, name='offer'),
    url(r'^choice/(?P<item_id>\d+)', choice, name='choice'),
    url(r'^trade/(?P<item_id>\d+)', trade),
    url(r'^offerAccept/(?P<offer_id>\d+)', accept),
    url(r'^offerDeny/(?P<offer_id>\d+)', deny),
    url(r'^', home, name='home'),
]