from django.urls import path
from book.views import *
from django.views.generic.base import TemplateView
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns =[
    
    path('',TemplateView.as_view(template_name='accounts/index.html'),name="accounts"),
    path('signup',SignupView.as_view(),name="Signup"),
    path('adminsignup',AdminSignupView.as_view(),name='adminsignup'),
    path('signin',SigninView.as_view(),name="Signin"),
    path('signout',SignoutView.as_view(),name="signout"),
    
    
]