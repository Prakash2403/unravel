from django.conf.urls import url
from .views import view_history

urlpatterns = [
    url(r'^history/$', view_history, name='history'),
]
