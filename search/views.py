from django.http import HttpResponse
from django.shortcuts import render

from youtube.models import Playlist, Trending


def search(request):
    query = request.GET.get('query')
    print(query)
    if query is not None:
        playlists = Playlist.objects.filter(title__contains=query)
        videos = Trending.objects.filter(title__contains=query).order_by("-rating")
        print(videos)
        context = {'playlists': playlists, 'videos': videos}
        return render(request, 'search/search_result.html', context=context)
    return HttpResponse("No search results found")
