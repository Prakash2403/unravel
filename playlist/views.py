from django.shortcuts import render

from youtube.models import Playlist


def view_playlist(request):
    playlist = Playlist.objects.all()
    categories = ["ML", "AI", "PP", "AD", "WD"]
    context = {'playlist': playlist, 'categories': categories}
    return render(request, 'playlist/Lecture.html', context=context)
