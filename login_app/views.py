from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import User_info,user_post
from .forms import UserPostStatus
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def login(request):
    return render(request,'login_app/login.html',{})

def raw_data(request):
    data = User_info.objects.all()
        
    
    return render(request,'login_app/login.html',{'data':data})
    return HttpResponse(str(data))


def login_auth(request):
    if request.method == "POST":
        
        
        uemail = request.POST.get("email")
        upassword = request.POST.get("psw")
        # return HttpResponse(upassword)
        try:
            user_logged = User_info.objects.get(email = uemail,password = upassword)
            request.session['user_id'] = user_logged.id
            messages.success(request,"Welcome")
            return redirect('homepage')
        except User_info.DoesNotExist:
            error = "Invalid"
            messages.error(request,error)
            return redirect('login')
    error = "Invalid"
    messages.error(request,error)
    return HttpResponse("Bypass")


def status(request):
    if request.method == 'POST':
        form = UserPostStatus(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status')
        else:
            return HttpResponse("Something Wrong")
    
    data = user_post.objects.all()
    return render(request,'login_app/NEW.html',{'data':data})
        
def signup(request):
    return render(request,'login_app/signup.html',{})
@csrf_exempt
def api_status(request):
    if request.method =="GET":
        data = user_post.objects.all()
        mydict = {}
        for item in data:
            mydict[item.author] = item.post
        return JsonResponse(mydict)
    elif request.method =="POST":
        body = request.body.decode('utf-8')
        author_name = json.loads(body)['username']
        post_msg = json.loads(body)['msg']
        user_post.objects.create(author = author_name,post= post_msg)
        mydict = {"msg":"DATA inserted.",author_name:post_msg}
        return JsonResponse(mydict)