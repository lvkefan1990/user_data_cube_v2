from django.shortcuts import render
from user_data_cube.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .db_search import *


# Create your views here.

def login_submit(request):
    if request.method == 'POST':
        username = request.POST["user_id"];
        password = request.POST["password"];
    user = authenticate(username = username,password = password);
    if user is not None:
        login(request,user);
        return render(request,"index.html",{"user_name": request.user.username});
    else:
        return render(request, "login.html", {"error":"您用户名或者密码错误"});


@login_required
@csrf_exempt
def wlgz_submit(request):
    get_value = request.POST["phone_number"];
    request.session["phone_number"] =get_value;
    dict_single_user=wlgz_db_search(get_value);
    return HttpResponse(json.dumps(dict_single_user, ensure_ascii=False), content_type="application/json,charset=utf-8");


@login_required
@csrf_exempt
def lssj_submit(request):
    get_value = request.POST["phone_number"];
    request.session["phone_number"] = get_value;
    lssj_dict=lssj_db_search(get_value);
    return HttpResponse(json.dumps(lssj_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def scpg_submit(request):
    get_value = request.POST["phone_number"];
    request.session["phone_number"] = get_value;
    scpg_dict = scpg_db_search(get_value);
    return HttpResponse(json.dumps(scpg_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def yhty_submit(request):
    get_value = request.POST["phone_number"];
    request.session["phone_number"] = get_value;
    yhty_dict = yhty_db_search(get_value);
    return HttpResponse(json.dumps(yhty_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");