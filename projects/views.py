from django.shortcuts import render


def view_projects(request):
    return render(request, 'projects/git1.html')
