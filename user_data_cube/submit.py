from django.shortcuts import render,render_to_response,HttpResponseRedirect
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
from django.http import JsonResponse
import datetime
from .select_option import *
import decimal
import pymysql
import pandas

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
        return HttpResponseRedirect('/index/') ;
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
                        return HttpResponseRedirect("/")
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
        "error": "正常",
    }
    #首先，获得用户输入的值
    if request.method =="POST":
        print(request.POST);
        city = request.POST["city"];
        district = request.POST["district"];
        formwork = request.POST["formwork"];
        round = RONUD_LIST.__len__()-1-int(request.POST["round"]);
        jlyhfx_dict["table_head"]=formwork_dict[formwork];
        print(jlyhfx_dict["table_head"]);
    conn = pymysql.connect(host='127.0.0.1', user='root', password='user_data_cube2019', database='user_data_cube');
    cur = conn.cursor();
    try:
        cur.callproc(procedure_dict[formwork],(city_dict[city],area_dict[city][district],RONUD_LIST[round]));
        result = cur.fetchall();
    except pymysql.err.InternalError:
        cur.callproc(procedure_dict[formwork], (city_dict[city], area_dict[city][district]))
        result = cur.fetchall()
    conn.close();
    for row in result:
        jlyhfx_dict["table_body"].append(list(row));
    #以上生成了返回页面的json数据，接下来写excel表格
    out = BytesIO();
    excel = pandas.ExcelWriter(out, engine='xlsxwriter');
    summary_df = pandas.DataFrame({});
    summary_df.to_excel(excel, sheet_name="查询内容", index=False, header=False);
    worksheet = excel.sheets["查询内容"];
    i = 0;
    while i < formwork_dict[formwork].__len__():
        worksheet.write(0, i, formwork_dict[formwork][i]);
        i += 1;
    # 写表体
    data_row = 1;
    while data_row<result.__len__()+1:
        col_index = 0;
        while col_index<result[0].__len__():
            if data_row<1048570:
                worksheet.write(data_row,col_index,result[data_row-1][col_index]);
            col_index+=1
        data_row +=1;
    excel.save();
    global export_excel;
    export_excel = HttpResponse(out.getvalue(), content_type='application/vnd.ms-excel');
    return HttpResponse(json.dumps(jlyhfx_dict,cls=DecimalEncoder ,ensure_ascii=False), content_type="application/json,charset=utf-8");

@login_required
@csrf_exempt
def jlyhfx_export_excel(request):
    export_excel['Content-Disposition'] = 'attachment;filename=聚类用户分析.xlsx',
    return export_excel;

@login_required
@csrf_exempt
def jlyhfx_onload(request):
    date_list = [];
    for state in STATE_LITE:
        date_str = str(state.year)+"-"+str(state.month)+"-"+str(state.day);
        date_list.append(date_str);
    date_list.reverse();#逆序输出
    jlyhfx_onload_dict = {"times":date_list}
    return HttpResponse(json.dumps(jlyhfx_onload_dict, ensure_ascii=False),content_type="application/json,charset=utf-8");


#自定义查询提交
zdycx_export = xlwt.Workbook(encoding='utf8');
@login_required
@csrf_exempt
def zdycx_submit(request):
    zdycx_table_dict = {
        "table_head": [],
        "table_body": [],
        "error":"正常",
    };
    get_value = request.POST;
    print(get_value);
    for value in get_value:
        if(get_value[value]==""):
            value_str = value;
            break;
    zdycx_dict = eval(value_str);
    condition_dict = zdycx_dict["condition"];
    col_list = zdycx_dict["result"];
    col_list.remove("起始时间");
    col_list.remove("终止时间");
    col_list.insert(3,"轮次");
    zdycx_table_dict["table_head"] = col_list;
    #接下来完成sql字符串的拼接
    zdycx_sql=r"with cte as (select usr_basic_info.CITY, usr_basic_info.AREA, usr_basic_info.MSISDN,usr_basic_info.ROUNDS FROM usr_basic_info ";#起头部分,结束默认空格
    #判断结果集合所涉及的表
    result_list_linshi=[];
    for col in col_list:
        if  col !="轮次":
            col_linshi = user_data_cube_fleld[col].split('.');
            result_list_linshi.append(col_linshi[0]);
    result_list = unique(result_list_linshi);
    print("所要查询的表为"+str(result_list));#result_list表示所要查询的表；
    if result_list.__len__()==1 and result_list[0]=='usr_basic_info':
        zdycx_sql = zdycx_sql + "where "
    else:
        for result_table in result_list:
            if result_table != 'usr_basic_info':
                inner_join = "inner join " + result_table + " ";
                zdycx_sql = zdycx_sql+ inner_join;
        zdycx_sql = zdycx_sql + "on ";
    for result_table in result_list:
        if result_table != 'usr_basic_info':
            on = "usr_basic_info.MSISDN = " + result_table + ".MSISDN and ";
            zdycx_sql = zdycx_sql + on;
    #至此电话号码的主键连接完成；下一步连接数据库获得rounds
    start_index = 0;
    j=STATE_LITE.__len__()-1;
    while start_index<STATE_LITE.__len__():
        if start_date_compare((int(condition_dict["起始时间"][0:4]),int(condition_dict["起始时间"][5:7]),int(condition_dict["起始时间"][8:10])),
                        (STATE_LITE[start_index].year,STATE_LITE[start_index].month,STATE_LITE[start_index].day)):
            break;
        else:
            start_index = start_index+1;
    #获得启示下标
    while j>=0:
        if end_date_compare((int(condition_dict["终止时间"][0:4]),int(condition_dict["终止时间"][5:7]),int(condition_dict["终止时间"][8:10])),
                        (STATE_LITE[j].year,STATE_LITE[j].month,STATE_LITE[j].day)):
            j = j-1;
        else:
            break;
    end_index = j+1;

    ronud_list = RONUD_LIST[start_index:end_index];#round_list是根据时间选择轮次
    if ronud_list.__len__()==1:
        zdycx_sql = zdycx_sql + "usr_basic_info.rounds in ('" + ronud_list[0] + "') and ";
    elif ronud_list.__len__()>1:
        round_str = str(tuple(ronud_list));
        zdycx_sql = zdycx_sql + "usr_basic_info.rounds in " + round_str + " and ";
    elif ronud_list.__len__() ==0:
        zdycx_table_dict["error"] = "您的所查询的时间段内没有数据"
        return HttpResponse(json.dumps(zdycx_table_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");
    #写内联的rounds

    for result_table in result_list:
        if result_table != 'usr_basic_info'and result_table != 'usr_resident_cell':
            ronud_inner = "usr_basic_info.rounds = "+result_table+".rounds and ";
            zdycx_sql = zdycx_sql+ronud_inner;
    #写地市和区县
    city=condition_dict['地市'];
    zdycx_sql = zdycx_sql+ "usr_basic_info.city in('"+city_dict[city]+"') and usr_basic_info.area in "
    xuqian =[];
    #判断区县的个数
    if condition_dict["区县"].__len__() <= 1:
        area = condition_dict["区县"][0]
        xuqian_str = "('"+area_dict[city][area]+"')"
    else:
        for dic in condition_dict["区县"]:
            xuqian.append(area_dict[city][dic]);
        xuqian_str = str(tuple(xuqian));
    zdycx_sql = zdycx_sql+ xuqian_str+")";
    #头部部分完成
    zdycx_sql = zdycx_sql + " select substring(cte.city,3), substring(cte.area,3), cte.msisdn, cte.rounds, ";
    co = 4;
    while co<col_list.__len__():
        zdycx_sql = zdycx_sql + user_data_cube_fleld[col_list[co]]+", ";
        co += 1;
    zdycx_sql = (zdycx_sql).rstrip(", ");
    zdycx_sql = zdycx_sql+" FROM cte "
    #结果查询部分完成,接下来写条件部分
    #先把条件所属表提取出来
    condition_table_linshi = [];
    for key in condition_dict:
        if key not in ["地市","区县","起始时间","终止时间","轮次"]:
            condition_table_linshi.append(user_data_cube_fleld[key].split(".")[0]);
    condition_table = unique(condition_table_linshi);#condition_table表示有条件选择的表
    print("有条件选择的表有"+str(condition_table));
    for result_table in result_list:
        #将结果表分为有条件选择的和没有条件选择的，不同对待
        if (result_table not in condition_table and result_table !='usr_resident_cell'):
            inner_join = " inner join "+result_table+" on cte.MSISDN = "+result_table+".MSISDN and cte.rounds ="+ result_table\
                        +".rounds  "#如果没加空格会出现andinner的情况
            print(inner_join);
            zdycx_sql = zdycx_sql + inner_join;
        elif result_table == 'usr_resident_cell':
            zdycx_sql = zdycx_sql +" inner join usr_resident_cell on cte.MSISDN = usr_resident_cell.MSISDN";
            if "用户常驻基站" in condition_dict and condition_dict["用户常驻基站"]!="":
                left_condition = " and "+user_data_cube_fleld["用户常驻基站"] + " LIKE '%" + str(condition_dict["用户常驻基站"]) + "%' ";
                zdycx_sql = zdycx_sql + left_condition;
            print(zdycx_sql);
        elif result_table != 'usr_basic_info' and (result_table in condition_table):
            inner_join = " inner join " + result_table + " on cte.MSISDN = " + result_table + ".MSISDN and cte.rounds =" + result_table \
                        + ".rounds and "
            for key in condition_dict:
                #范围类
                if key not in ["地市","区县","起始时间","终止时间","轮次","平均RSRP"] and user_data_cube_fleld[key].split(".")[0] == result_table\
                        and type(condition_dict[key]) == list:
                    left_condition = user_data_cube_fleld[key]+" BETWEEN "+str(condition_dict[key][0])+" and "+ str(condition_dict[key][1])+" and ";
                    inner_join = inner_join + left_condition;
                elif key =="平均RSRP" and user_data_cube_fleld[key].split(".")[0] == result_table\
                        and type(condition_dict[key]) == list:
                    left_condition = user_data_cube_fleld[key]+" BETWEEN "+str(float(condition_dict[key][0])+140)+" and "+ str(float(condition_dict[key][1])+140)+" and ";
                    inner_join = inner_join + left_condition;
                #单选类
                elif  key not in ["地市","区县","起始时间","终止时间","轮次","平均RSRP"] and user_data_cube_fleld[key].split(".")[0] == result_table\
                        and type(condition_dict[key]) == str and condition_dict[key] !="全选":
                    left_condition = user_data_cube_fleld[key] + " in " + yes_or_no[str(condition_dict[key])]+ " and ";
                    inner_join = inner_join + left_condition;
            inner_join = inner_join.rstrip("and ")
            print(inner_join);
            zdycx_sql = zdycx_sql + inner_join;

    print(zdycx_sql[0:300]);
    print(zdycx_sql[300:600]);
    print(zdycx_sql[600:900]);
    print(zdycx_sql[900:]);
    #以下是数据导出部分
    conn = pymysql.connect(host='127.0.0.1', user='root', password='user_data_cube2019', database='user_data_cube');
    cur = conn.cursor();
    if zdycx_sql[-4:] =="and ":
        cur.execute(zdycx_sql[:-4]);
    else :
        cur.execute(zdycx_sql);
    result = cur.fetchall();
    conn.close();
    #写导出的表格
    """wb = xlwt.Workbook(encoding='utf8');
    sheet = wb.add_sheet('查询结果');
    #写表头
    i = 0;
    while i <col_list .__len__():
        sheet.write(0, i, col_list[i]);
        i += 1;
    #写表体
    data_row = 1;
    for row in result:
        zdycx_table_dict["table_body"].append(list(row));#写入字典
        col_index =0;
        while col_index < result[0].__len__():
            sheet.write(data_row, col_index,row[col_index]);
            col_index += 1
        data_row += 1;
    global zdycx_export;
    zdycx_export = wb;"""
    """out = BytesIO();
    excel = pandas.ExcelWriter(out, engine='xlsxwriter');
    summary_df = pandas.DataFrame({});
    summary_df.to_excel(excel, sheet_name="查询内容", index=False, header=False);
    worksheet = excel.sheets["查询内容"];
    excel.save();
    #以上6行代码表示将xlsx保存到out中"""
    out = BytesIO();
    excel = pandas.ExcelWriter(out, engine='xlsxwriter');
    summary_df = pandas.DataFrame({});
    summary_df.to_excel(excel, sheet_name="查询内容", index=False, header=False);
    worksheet = excel.sheets["查询内容"];
    # 写表头
    i = 0;
    while i < col_list.__len__():
        worksheet.write(0, i, col_list[i]);
        i += 1;
    # 写表体
    data_row = 1;
    for row in result:
        zdycx_table_dict["table_body"].append(list(row));  # 写入字典
        col_index = 0;
        while col_index < result[0].__len__():
            if col_index<1048570:
                worksheet.write(data_row, col_index, row[col_index]);
            col_index += 1
        data_row += 1;
    excel.save();
    global zdycx_export;
    zdycx_export = HttpResponse(out.getvalue(), content_type='application/vnd.ms-excel');
    return HttpResponse(json.dumps(zdycx_table_dict, ensure_ascii=False), content_type="application/json,charset=utf-8");

#自定义查询页面的表格导出
@login_required
@csrf_exempt
def zdycx_export_excel(request):
    zdycx_export['Content-Disposition'] = 'attachment;filename=自定义查询.xlsx',
    return zdycx_export;