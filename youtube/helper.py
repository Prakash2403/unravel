from django.contrib.auth.models import User
from .models import Trending, History, Channel, Playlist
from .search import youtube_search
import pafy

YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v='
YOUTUBE_PLAYLIST_URL = 'https://www.youtube.com/playlist/?list='


def get_channel_obj(search_result):
    channel_obj = Channel()
    channel_obj.channel_id = search_result["snippet"]["channelId"]
    channel_obj.channel_name = search_result["snippet"]["channelTitle"]
    return channel_obj


def get_video_obj(search_result):
    channel_obj = get_channel_obj(search_result)
    channel_obj.save()
    channel_obj.refresh_from_db()
    video_obj = Trending()
    video_obj.title = search_result["snippet"]["title"]
    video_obj.thumbnail = search_result["snippet"]["thumbnails"]["high"]["url"]
    video_obj.video_id = YOUTUBE_VIDEO_URL + search_result["id"]["videoId"]
    video_obj.description = search_result["snippet"]["description"]
    video_obj.channel = channel_obj
    metadata = get_video_metadata(video_obj.video_id)
    video_obj.likes = metadata['likes']
    video_obj.dislikes = metadata['dislikes']
    video_obj.views = metadata['views']
    return video_obj


def update_trending_db():
    video_obj_list = []
    search_response = youtube_search("Machine Learning")
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_obj = get_video_obj(search_result)
            video_obj_list.append(video_obj)
    if len(video_obj_list) != 0:
        Trending.objects.all().delete()
    for video_obj in video_obj_list:
        video_obj.save()


def update_history(username, video_url):
    user = User.objects.get(username=username)
    history_obj = History()
    history_obj.user = user
    history_obj.video_url = video_url[1:(len(video_url) - 1)]
    history_obj.save()


def get_video_metadata(url):
    video = pafy.new(url)
    return {
            'likes': video.likes,
            'dislikes': video.dislikes,
            'views': video.viewcount
           }


def update_playlist_db(playlist_id, domain):
    playlist = pafy.get_playlist2(playlist_url=YOUTUBE_PLAYLIST_URL+playlist_id)
    playlist_obj = Playlist()
    playlist_obj.domain = domain
    playlist_obj.author = playlist.author
    playlist_obj.title = playlist.title
    playlist_obj.description = playlist.description
    playlist = pafy.get_playlist(playlist_url=YOUTUBE_PLAYLIST_URL+playlist_id)
    playlist_obj.thumbnail_url = playlist['items'][0]['pafy'].thumb
    playlist_obj.num_videos = len(playlist['items'])
    playlist_obj.save()


def get_playlist_db():
    search_response = youtube_search("Machine Learning")
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#playlist":
            update_playlist_db(search_result["id"]["playlistId"], "ML")
