from django.shortcuts import render, redirect

from youtube.helper import update_history
from youtube.models import Trending


def trending(request):
    trending_videos = Trending.objects.all()[:10]
    context = {'trending': trending_videos}
    return render(request=request, template_name='index/index.html', context=context)


def redirect_to_youtube(request):
    update_history(request.user, request.GET.get('video_url'))
    video_url = request.GET.get('video_url')
    print(video_url[1:(len(video_url) - 1)]) # For excluding single inverted commas
    return redirect(video_url[1: len(video_url) - 1])
