from django.db import models

from user.models import User


class Channel(models.Model):
    channel_id = models.CharField(max_length=50, primary_key=True)
    channel_name = models.CharField(max_length=50)

    def __str__(self):
        return self.channel_name


class Trending(models.Model):
    thumbnail = models.URLField()
    description = models.TextField(max_length=5000)
    title = models.CharField(max_length=100)
    video_id = models.URLField(primary_key=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    likes = models.BigIntegerField()
    dislikes = models.BigIntegerField()
    views = models.BigIntegerField()

    def __str__(self):
        return self.title


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    thumbnail_url = models.URLField()
    num_videos = models.IntegerField()
    domain = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
