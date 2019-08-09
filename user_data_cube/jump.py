from django.shortcuts import render
from django.http import HttpResponse
from . import models,db_search
from user_data_cube.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import json

#import inspect#用于得到model中所有的类



# Create your views here.

def user_login(request):
    request.session["phone_number"]="";
    return render(request, "login.html");

@login_required
def index(request):
    return render_to_response("index.html",{"user_name":request.user.username});

@login_required
def xgmm(request):
    print(request.session["phone_number"])
    return render(request,"xgmm.html")

@login_required
def wlgz(request):
    print("网络感知时刻："+str(request.session["phone_number"]));
    return render(request,"wlgz.html");

@login_required
def lssj(request):
    print("历史数据时刻："+str(request.session["phone_number"]));
    return render(request,"lssj.html");

@login_required
def scpg(request):
    print("市场评估时刻：",request.session["phone_number"]);
    return render(request,"scpg.html");

@login_required
def yhty(request):
    print("用户体验时刻：",request.session["phone_number"]);
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

@login_required
@csrf_exempt
def wlgz_onload(request):
    print("网络感知加载：", request.session["phone_number"]);
    wlgz_dict=db_search.wlgz_db_search(request.session["phone_number"])
    return HttpResponse(json.dumps(wlgz_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def lssj_onload(request):
    print("历史数据加载：", request.session["phone_number"]);
    lssj_dict=db_search.lssj_db_search(request.session["phone_number"])
    return HttpResponse(json.dumps(lssj_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def scpg_onload(request):
    print("市场评估加载：", request.session["phone_number"]);
    scpg_dict=db_search.scpg_db_search(request.session["phone_number"])
    print(request.session["phone_number"]);
    return HttpResponse(json.dumps(scpg_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def yhty_onload(request):
    print("用户体验加载：", request.session["phone_number"]);
    yhty_dict=db_search.yhty_db_search(request.session["phone_number"])
    return HttpResponse(json.dumps(yhty_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");