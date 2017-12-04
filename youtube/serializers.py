from rest_framework import serializers

from youtube.models import Trending


class YoutubeTrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trending
        fields = ('thumbnail', 'title', 'video_id')
