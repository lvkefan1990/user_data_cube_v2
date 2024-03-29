from django.shortcuts import render,HttpResponseRedirect,HttpResponse
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
    #print(request.user.is_anonymous);判断是否匿名用户
    #print(request.user.is_authenticated);判断是否登录
    request.session["phone_number"] = "";#清空phone_number
    return render(request, "login.html");

@login_required
def index(request):
    print(request.user);
    return render_to_response("index.html",{"user_name":request.user.username});

@login_required
def xgmm(request):
    return render(request,"xgmm.html")

@login_required
def wlgz(request):
    return render(request,"wlgz.html");

@login_required
def lssj(request):
    return render(request,"lssj.html");

@login_required
def scpg(request):
    return render(request,"scpg.html");

@login_required
def yhty(request):
    return render(request,"yhty.html");

@login_required
def jlyhfx(requset):
    return render(requset,"jlyhfx.html")

@login_required
def zdycx(requset):
    return render(requset,"zdycx.html")

@login_required
def change_password(request):
    return render("login.html");

@login_required
@csrf_exempt
def jlyhfx(request):
    return render_to_response("jlyhfx.html", {"user_name": request.user.username});

@login_required
@csrf_exempt
def zdycx(request):
    return render_to_response("zdycx.html", {"user_name": request.user.username});

@login_required
def exit(request):
    logout(request);
    print(request.method);
    return render(request,"login.html");

@login_required
@csrf_exempt
def wlgz_onload(request):
    wlgz_dict=db_search.wlgz_db_search(request.session["phone_number"])
    return HttpResponse(json.dumps(wlgz_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def lssj_onload(request):
    lssj_dict=db_search.lssj_db_search(request.session["phone_number"])
    return HttpResponse(json.dumps(lssj_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def scpg_onload(request):
    scpg_dict=db_search.scpg_db_search(request.session["phone_number"])
    return HttpResponse(json.dumps(scpg_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def yhty_onload(request):
    print(request.session["phone_number"]);
    yhty_dict=db_search.yhty_db_search(request.session["phone_number"])
    return HttpResponse(json.dumps(yhty_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");


def pageNotFound(request,exception):
    '''
    404、500处理函数
    '''
    return render_to_response('404.html')

def error_404(request):
    '''
    404、500处理函数
    '''
    if request.user.is_authenticated == True:
        return HttpResponseRedirect(r'/index/');
    else:
        return HttpResponseRedirect("/");



