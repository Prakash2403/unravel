from rest_framework import serializers

from youtube.models import Trending, Playlist


class YoutubeTrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trending
        fields = ('thumbnail', 'title', 'video_id', 'channel', 'description',
                  'likes', 'dislikes', 'views')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('title', 'author', 'thumbnail_url', 'num_videos', 'description', 'playlist_url')
