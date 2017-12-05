from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from youtube.models import Trending, Playlist
from youtube.serializers import YoutubeTrendingSerializer, PlaylistSerializer


@csrf_exempt
def trending_list(request):
    if request.method == 'GET':
        trending = Trending.objects.all()[:10]
        serializer = YoutubeTrendingSerializer(trending, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        raise PermissionDenied()


@csrf_exempt
def playlist(request):
    if request.method == 'GET':
        domain = request.GET.get('domain')
        print(domain)
        playlist = Playlist.objects.filter(domain=domain)
        serializer = PlaylistSerializer(playlist, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        raise PermissionDenied()
