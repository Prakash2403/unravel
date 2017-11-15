from django.db import models


class Trending(models.Model):
    thumbnail = models.URLField()
    title = models.CharField(max_length=100)
    video_id = models.URLField(primary_key=True)
