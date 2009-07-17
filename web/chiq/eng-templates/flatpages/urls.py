from django.conf.urls.defaults import *
from chiq.settings import WEB_URL

root = "/".join(WEB_URL.split("/")[3:]) 

urlpatterns = patterns('chiq.flatpages.views', (r'^%s/(?P<url>.*)$' % root, 'flatpage'),)
