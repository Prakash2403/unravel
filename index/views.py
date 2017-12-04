from django.shortcuts import render

from youtube.models import Trending


def trending(request):
    trending_videos = Trending.objects.all()[:10]
    context = {'trending': trending_videos}
    return render(request=request, template_name='index/index.html', context=context)
