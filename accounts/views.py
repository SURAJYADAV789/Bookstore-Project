from audioop import reverse
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic.edit import CreateView
from accounts.forms import MyAdminCreationForm, MyUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import MyUser


# Create your views here.

class SignupView(CreateView):
    model=MyUser
    form_class=MyUserCreationForm
    template_name='accounts/signup.html'
    success_url=reverse_lazy('home')

class AdminSignupView(CreateView):
    model=MyUser
    form_class=MyAdminCreationForm
    template_name='accounts/signin.html'
    success_url=reverse_lazy('accounts')
    success_message='Staff Member Addred Succesfully'


class SigninView(LoginView):
    model=MyUser
    template_name='accounts/signin.html'
    success_url=reverse_lazy('home')
    success_message='Your Login succesfully'


class SignoutView(LogoutView):
    template_name='book/home.html'
    success_message='Logout  is succesfully'


