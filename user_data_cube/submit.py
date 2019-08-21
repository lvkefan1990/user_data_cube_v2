from django.shortcuts import render
from user_data_cube.models import *
from .db_search import *
from .location import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
import xlwt
from io import BytesIO
import decimal
from django.http import JsonResponse
import datetime


# Create your views here.

#Decimal错误解决办法
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

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

#先声明一个全局变量
export_excel = xlwt.Workbook(encoding='utf8');
@login_required
@csrf_exempt
def jlyhfx_submit(request):
    jlyhfx_dict={
        "table_head":[],
        "table_body":[],
    }
    #首先，获得用户输入的值
    if request.method =="POST":
        print(request.POST);
        city = request.POST["city"];
        district = request.POST["district"];
        formwork = request.POST["formwork"];
        round = int(request.POST["round"]);
        jlyhfx_dict["table_head"]=formwork_dict[formwork];
        print(jlyhfx_dict["table_head"]);
    import pymysql
    conn = pymysql.connect(host='127.0.0.1', user='root', password='user_data_cube2019', database='user_data_cube');
    cur = conn.cursor();
    try:
        cur.callproc(procedure_dict[formwork],(city_dict[city],area_dict[city][district],RONUD_LIST[round]));
        result = cur.fetchall();
    except pymysql.err.InternalError:
        cur.callproc(procedure_dict[formwork], (city_dict[city], area_dict[city][district]))
        result = cur.fetchall()
    for row in result:
        print(row);
        jlyhfx_dict["table_body"].append(list(row));
    #以上生成了返回页面的json数据，接下来写excel表格
    wb = xlwt.Workbook(encoding='utf8');
    sheet = wb.add_sheet('查询结果');
    i = 0;
    while i < formwork_dict[formwork].__len__():
        sheet.write(0, i, formwork_dict[formwork][i]);
        i += 1;
    data_row = 1;
    while data_row<result.__len__()+1:
        col_index = 0;
        while col_index<result[0].__len__():
            sheet.write(data_row,col_index,result[data_row-1][col_index]);
            col_index+=1
        data_row +=1;
    global export_excel;
    export_excel = wb;
    return HttpResponse(json.dumps(jlyhfx_dict, cls=DecimalEncoder,ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def jlyhfx_export_excel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel');
    response['Content-Disposition'] = 'attachment;filename=search_result.xls';
    output = BytesIO();
    export_excel.save(output);
    output.seek(0);
    response.write(output.getvalue());
    return response;

#分页的测试
def page(request):
    return render(request,"paginator_test.html");