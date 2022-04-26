from dataclasses import field
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.contrib.auth.views import LoginView

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('fname','lname','contact','email','password1','password2','address')

class MyAdminCreationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('fname','lname','contact','email','role','password1','password2','address')
