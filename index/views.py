from django.shortcuts import render


def trending(request):
    return render(request=request, template_name='index/index.html')
