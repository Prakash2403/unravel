from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^snippets/$', views.trending_list),
]
