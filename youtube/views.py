from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from youtube.models import History


@login_required
def view_history(request):
    username = request.user.username
    history = History.objects.filter(user__username=username)
    context = {'history': history}
    return render(request, 'youtube/history.html', context=context)
