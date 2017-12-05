from django.contrib.auth.models import User

from .models import Trending, History
from .search import youtube_search

YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v='


def update_trending_db():
    video_obj_list = []
    search_response = youtube_search("Machine Learning")
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_obj = Trending()
            video_obj.title = search_result["snippet"]["title"]
            video_obj.thumbnail = search_result["snippet"]["thumbnails"]["default"]["url"]
            video_obj.video_id = YOUTUBE_VIDEO_URL + search_result["id"]["videoId"]
            video_obj_list.append(video_obj)
    if len(video_obj_list) != 0:
        Trending.objects.all().delete()
    for video_obj in video_obj_list:
        video_obj.save()


def update_history(usernanme, video_url):
    user = User.objects.get(username=usernanme)
    history_obj = History()
    history_obj.user = user
    history_obj.video_url = video_url[1:(len(video_url)-1)]
    history_obj.save()
