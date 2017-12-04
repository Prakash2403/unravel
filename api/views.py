from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from youtube.models import Trending
from youtube.serializers import YoutubeTrendingSerializer


@csrf_exempt
def trending_list(request):
    if request.method == 'GET':
        trending = Trending.objects.all()[:10]
        serializer = YoutubeTrendingSerializer(trending, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        raise PermissionDenied("You are not allowed to make a POST request")
