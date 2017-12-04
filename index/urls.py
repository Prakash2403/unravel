from django.conf.urls import url

from index.views import trending, redirect_to_youtube

urlpatterns = [
    url(r'^redirect/', redirect_to_youtube),
    url(r'^$', trending),
    ]
