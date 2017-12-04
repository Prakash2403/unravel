from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.email = form.cleaned_data.get('email_id')
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
