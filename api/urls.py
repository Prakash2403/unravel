from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^trending/$', views.trending_list),
    url(r'^playlist/', views.playlist)
]
