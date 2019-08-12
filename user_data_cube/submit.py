from django.shortcuts import render
from user_data_cube.models import *
from .db_search import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from numpy import transpose
import datetime

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

#密码强度判断代码
def checkio(s):
    fs = ''.join(filter(str.isalnum, s)) # keep only letters and digits
    return (len(fs) >= 1        # 至少有一位字符
        and len(s)  >= 8       # ...字符串长度至少为8位
        and not fs.isalpha()    # ... 至少有一个数字
        and not fs.isdigit())    # ... 至少有一个字母


@login_required
def change_password(request):
    if request.method == 'POST':
        oldpassword = request.POST["oldpassword"]
        newpassword = request.POST["newpassword"]
        commitpassword = request.POST["commitpassword"]
        #判断输入密码是否和原密码相同
        if request.user.check_password(oldpassword) == True:
            #判断两次输入的密码是否相同
            if commitpassword == newpassword:
                #判断新密码是否与原密码一样
                if request.user.check_password(newpassword) == True:
                    return render(request, "xgmm.html",{"error":"您输入的新密码与原始密码不能相同"})
                else:
                    # 判断字符串密码强度
                    if checkio(newpassword):
                        user = request.user
                        user.set_password(newpassword)
                        user.save()
                        return render(request, "login.html")
                    else:
                        return render(request, "xgmm.html", {"error":"您输入的密码强度不足"})
            else:
                return render(request,"xgmm.html",{"error":"您再次输入的密码与新密码不一致"})
        else:
            return render(request, "xgmm.html", {"error":"您输入的原始密码不正确"})
    return render(request, "xgmm.html")

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
    #返回lssj_dict
    return HttpResponse(json.dumps(lssj_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def scpg_submit(request):
    get_value = request.POST["phone_number"];
    request.session["phone_number"] = get_value;
    scpg_dict=scpg_db_search(get_value);
    return HttpResponse(json.dumps(scpg_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def yhty_submit(request):
    get_value = request.POST["phone_number"];
    request.session["phone_number"] = get_value;
    yhty_dict=yhty_db_search(get_value);
    return HttpResponse(json.dumps(yhty_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");