from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from manae_users_demos.auth_app.models import ToDo


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label='Remember me')


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'description']
