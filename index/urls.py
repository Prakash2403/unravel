from django.conf.urls import url

from index.views import trending

urlpatterns = [
    url(r'^$', trending),
    ]
