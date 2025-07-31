from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'login_app/index.html',{})
