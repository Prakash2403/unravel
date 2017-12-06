from django.conf.urls import url
from .views import view_playlist

urlpatterns = [
    url(r'^$', view_playlist, name='signup'),
]
