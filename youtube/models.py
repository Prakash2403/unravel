from django.db import models

from user.models import User


class Trending(models.Model):
    thumbnail = models.URLField()
    title = models.CharField(max_length=100)
    video_id = models.URLField(primary_key=True)


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username
