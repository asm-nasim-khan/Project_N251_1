from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login,name="login"),
    path('login_auth', views.login_auth,name="login_auth"),
    path('status', views.status,name="status"),
    path('signup', views.signup,name="signup"),
    path('api', views.api_status,name="api"),
    
    
    
    
]
