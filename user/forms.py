from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email_id = forms.EmailField(help_text='Enter your email here.')
    birth_date = forms.DateField(help_text='Enter your DoB')

    class Meta:
        model = User
        fields = ('username', 'email_id', 'birth_date', 'password1', 'password2', )
