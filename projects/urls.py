from django.conf.urls import url
from .views import view_projects

urlpatterns = [
    url(r'^$', view_projects, name='projects'),
]
