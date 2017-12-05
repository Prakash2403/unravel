from django.contrib import admin

from youtube.models import History, Trending, Channel, Playlist

admin.site.register(History)
admin.site.register(Trending)
admin.site.register(Channel)
admin.site.register(Playlist)
