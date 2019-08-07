from django.shortcuts import render
from . import models
from user_data_cube.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import inspect#用于得到model中所有的类

# Create your views here.

def user_login(request):
    request.session["phone_number"]="";
    print(request.session["phone_number"]);
    return render(request, "login.html");

@login_required
def index(request):
    print(request.session["phone_number"]);
    return render_to_response("index.html",{"user_name":request.user.username});

@login_required
def wlgz(request):
    print(request.session["phone_number"]);
    return render(request,"wlgz.html");

@login_required
def lssj(request):
    print(request.session["phone_number"]);
    return render(request,"lssj.html");

@login_required
def scpg(request):
    print(request.session["phone_number"]);
    return render(request,"scpg.html");

@login_required
def yhty(request):
    print(request.session["phone_number"]);
    return render(request,"yhty.html");

@login_required
def change_password(request):
    print(request.session["phone_number"]);
    return render_to_response("change_password.html",{"user_name":request.user.username});

@login_required
def exit(request):
    print(request.session["phone_number"]);
    logout(request);
    print(dir(request.user));
    return render(request,"login.html");