from django.shortcuts import render, redirect

from youtube.helper import update_history
from youtube.models import Trending, Playlist


def trending(request):
    trending_videos = Trending.objects.all().order_by('-rating')[:12]
    trending_python = Trending.objects.filter(title__contains='Python').order_by('-rating')[:12]
    context = {'trending': trending_videos, 'trending_python': trending_python}
    return render(request=request, template_name='index/index.html', context=context)


def redirect_to_youtube(request):
    print(request.user.username)
    if request.user.username:
        update_history(request.user, request.GET.get('video_url'))
    video_url = request.GET.get('video_url')
    return redirect(video_url[1: len(video_url) - 1])
