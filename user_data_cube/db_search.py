from user_data_cube.models import *
from numpy import transpose



RONUD_LIST=[];#轮次列表
STATE_LITE=[];#时间轮次
rounds_nomean=RoundsLog.objects.filter();
for ronud_item in rounds_nomean:
    RONUD_LIST.append(ronud_item.rounds);
    STATE_LITE.append(ronud_item.sdate);

RECENT_ROUND = RONUD_LIST[-1];#最近的轮次
RECENT_TIME = STATE_LITE[-1];#最近一轮的时间

def start_date_compare(start=(0,0,0),end=(0,0,0)):
    """
    :param start:起始时间
    :param end:结束时间
    :return:起始时间小于或者等于结束时间则返回TRUE
    """
    i = 0;
    while i<start.__len__():
        if start[i]<end[i]:
            return True;
        elif start[i]>end[i]:
            return False;
        elif start[i] == end[i]:
            if i != start.__len__()-1:
                i +=1;
            else:
                #相等的情况,如果日期相等返回True
                return True;

def end_date_compare(start=(0,0,0),end=(0,0,0)):
    """
    :param start:起始时间
    :param end:结束时间
    :return:起始时间小于或者等于结束时间则返回False
    """
    i = 0;
    while i<start.__len__():
        if start[i]<end[i]:
            return True;
        elif start[i]>end[i]:
            return False;
        elif start[i] == end[i]:
            if i != start.__len__()-1:
                i +=1;
            else:
                #相等的情况,如果日期相等返回True
                return False;



#该函数封装了用户基本表的查询功能
def user_basic_info(phone_number):
    dict_user_basic = {
        "phonemuber": "",
        "user_city": "该数据缺失",
        "district": "该数据缺失",
        "county": "该数据缺失",
        "citizen_or_villager": "该数据缺失",
        "star": "该数据缺失",
        "begin": "该数据缺失",
        "length_of_time": "该数据缺失",
        "phone_brand": "该数据缺失",
        "is_header_user": "该数据缺失",
        "is_risk_user": "该数据缺失",
        "phone_type": "该数据缺失",
        "is_complaint_user":"该数据缺失",
        "is_discontent_user": "该数据缺失",
        "resident_cell":"该数据缺失",
        "error_text": "正常",
    }
    try:
        single_UsrBasicInfo = UsrBasicInfo.objects.get(msisdn=phone_number,rounds=RECENT_ROUND);
    except ValueError:
        dict_user_basic["error_text"] = "您的输入错误，请重新输入";
        return dict_user_basic;
    except UsrBasicInfo.DoesNotExist:
        dict_user_basic["error_text"] = "对不起，查询不到您所需要的数据";
        return dict_user_basic;
    dict_user_basic["phonemuber"] = single_UsrBasicInfo.msisdn;
    dict_user_basic["user_city"] = single_UsrBasicInfo.city[2:5];
    dict_user_basic["district"] = single_UsrBasicInfo.area[2:];
    dict_user_basic["county"] = single_UsrBasicInfo.area1;
    dict_user_basic["citizen_or_villager"] = single_UsrBasicInfo.overlay_area;
    dict_user_basic["star"] = single_UsrBasicInfo.star_type;
    dict_user_basic["begin"] = single_UsrBasicInfo.start_date[:4] + "年" + single_UsrBasicInfo.start_date[4:6] + "月"\
                               + single_UsrBasicInfo.start_date[6:] + "日";
    dict_user_basic["length_of_time"] = str(single_UsrBasicInfo.online_time) + "个月";
    try:
        single_TacImeiRelation = TacImeiRelation.objects.get(msisdn=phone_number,rounds=RECENT_ROUND);
    except ValueError:
        pass;
    except TacImeiRelation.DoesNotExist:
        pass;
    else:
        if single_TacImeiRelation.brand!=None and single_TacImeiRelation.type != None:
            dict_user_basic["phone_brand"]=single_TacImeiRelation.brand;
            dict_user_basic["phone_type"] = single_TacImeiRelation.type;
    # 查询用户是否是头部用户
    try:
        single_UsrExpenses = UsrExpenses.objects.get(msisdn=phone_number, rounds=RECENT_ROUND);
    except ValueError:
        pass;
    except UsrExpenses.DoesNotExist:
        pass;
    else:
        if single_UsrExpenses.if_30_arpu != 1:
            dict_user_basic["is_header_user"] = "否";
        else:
            dict_user_basic["is_header_user"] = "是";
    #是否高危用户
    try:
        single_UsrCompltRecord = UsrCompltRecord.objects.get(msisdn=phone_number, rounds=RECENT_ROUND);
    except ValueError:
        pass;
    except UsrCompltRecord.DoesNotExist:
        pass;
    else:
        if single_UsrCompltRecord.if_risk_user != 1:
            dict_user_basic["is_risk_user"] = "否";
        else:
            dict_user_basic["is_risk_user"] = "是";
        if single_UsrCompltRecord.if_complaint_user != 1:
            dict_user_basic["is_complaint_user"] = "否";
        else:
            dict_user_basic["is_complaint_user"] = "是";
        if single_UsrCompltRecord.if_discontent_user != 1:
            dict_user_basic["is_discontent_user"] = "否";
        else:
            dict_user_basic["is_discontent_user"] = "是";
    #查询用户常驻基站
    try:
        resident_l = UsrResidentCell.objects.get(msisdn=phone_number);
    except ValueError:
        pass
    except UsrResidentCell.DoesNotExist:
        pass;
    else:
        resident_cell = CellParaTable.objects.filter(enodeb_id=resident_l.enodeb_id).values('enodeb_name').distinct();
        dict_user_basic["resident_cell"]=resident_cell[0]['enodeb_name'];
    return dict_user_basic;

def wlgz_db_search(get_value):
    dict_single_user = {
        "coverage": "该数据缺失",
        "rsrp": "该数据缺失",
        "dl_speed": "该数据缺失",
        "call_success": "该数据缺失",
        "yhczxq":"该数据缺失",#用户常驻小区
        "fgl":"该数据缺失",#覆盖率
        "cphrl":"该数据缺失",#差phr率
        "xhcgl":"该数据缺失",#寻呼成功率
        "dxl":"该数据缺失",#掉话率
        "qywsxsl":"该数据缺失",#全业务上行速率
        "dbsxsl":"该数据缺失",#大包上行速率
        "dbxxsl": "该数据缺失",  # 大包下行速率
        "httpcgl":"该数据缺失",#HTTP响应成功率
        "tcpcgl":"该数据缺失",#TCP成功率
        "tcpsy":"该数据缺失",#TCP时延
        "tcpwxcgl":"该数据缺失",#TCP无线成功率
        "tcpwxsy":"该数据缺失",#TCP无线时延
        "ymxysy":"该数据缺失",#页面响应时延
        "qhcgl":"该数据缺失",#切换成功率
        "fwqqcgl": "该数据缺失",  # 服务请求成功率
        "fzcgl":"该数据缺失",#附着成功率
        "tau":"该数据缺失",#TAU成功率
    }
    dict_user_basic=user_basic_info(get_value);
    #查询用户覆盖信息
    try:
        single_UsrCoverPecpt = UsrCoverPecpt.objects.get(msisdn=get_value,rounds=RECENT_ROUND);
    except ValueError:
        pass
    except UsrCoverPecpt.DoesNotExist:
        pass;
    else:
        if (single_UsrCoverPecpt.poor_point != None and single_UsrCoverPecpt.sum_point != None
            and single_UsrCoverPecpt.weak_point != None):
            bad_cover=round(single_UsrCoverPecpt.poor_point/single_UsrCoverPecpt.sum_point,2);
            middle_cover = round(single_UsrCoverPecpt.weak_point/single_UsrCoverPecpt.sum_point,2);
            good_cover = 1-bad_cover-middle_cover;
            dict_single_user["coverage"] = [{"name":'优',"value":good_cover},
                                            {"name":'良',"value":middle_cover},
                                            {"name":'差',"value":bad_cover}];
            #查询用户rsrp
            dict_single_user["fgl"]=good_cover;
            dict_single_user["rsrp"] = single_UsrCoverPecpt.avg_rsrp;
            dict_single_user["cphrl"]=single_UsrCoverPecpt.bad_phr_rate;

    #用户上下行速率，大包速率
    try:
        single_UsrSpeedPecpt = UsrSpeedPecpt.objects.get(msisdn=get_value,rounds=RECENT_ROUND);
    except ValueError:
        pass
    except UsrSpeedPecpt.DoesNotExist:
        pass;
    else:
        dict_single_user["dl_speed"] = single_UsrSpeedPecpt.dl_speed;
        dict_single_user["qywsxsl"] = single_UsrSpeedPecpt.ul_speed;
        dict_single_user["dbsxsl"] = single_UsrSpeedPecpt.bp_ul_speed;
        dict_single_user["dbxxsl"] = single_UsrSpeedPecpt.bp_dl_speed;
    #核心网数据
    try:
        single_UsrCorePecpt = UsrCorePecpt.objects.get(msisdn=get_value,rounds=RECENT_ROUND);
    except ValueError:
        pass
    except UsrCorePecpt.DoesNotExist:
        pass;
    else:
        dict_single_user["qhcgl"] = single_UsrCorePecpt.ho_rate;
        dict_single_user["fwqqcgl"] = single_UsrCorePecpt.sr_rate;
        dict_single_user["fzcgl"] = single_UsrCorePecpt.attach_rate;
        dict_single_user["tau"] = single_UsrCorePecpt.tau_rate;

    #用户通话成功率
    try:
        single_UsrCallPecpt = UsrCallPecpt.objects.get(msisdn=get_value,rounds=RECENT_ROUND);
    except ValueError:
        pass
    except UsrCallPecpt.DoesNotExist:
        pass;
    else:
        dict_single_user["xhcgl"] = round(single_UsrCallPecpt.paging_rate, 2);
        dict_single_user["dxl"] = round(single_UsrCallPecpt.dc_rate, 2);
        dict_single_user["call_success"] = round(single_UsrCallPecpt.paging_rate*(1-single_UsrCallPecpt.dc_rate),2);
    #查询用户端到端数据
    try:
        single_UsrEtePecpt = UsrEtePecpt.objects.get(msisdn=get_value,rounds=RECENT_ROUND);
    except ValueError:
        pass;
    except UsrEtePecpt.DoesNotExist:
        pass;
    else:
        dict_single_user["httpcgl"]=single_UsrEtePecpt.http_res_rate;
        dict_single_user["tcpcgl"] = single_UsrEtePecpt.tcp_core_rate;
        dict_single_user["tcpsy"] = single_UsrEtePecpt.tcp_core_delay;
        dict_single_user["tcpwxcgl"] = single_UsrEtePecpt.tcp_radio_rate;
        dict_single_user["tcpwxsy"] = single_UsrEtePecpt.tcp_radio_delay;
        dict_single_user["ymxysy"]=single_UsrEtePecpt.page_res_delay;
    dict_single_user.update(dict_user_basic)
    return dict_single_user;

def lssj_db_search(get_value):
    dict_user_basic = user_basic_info(get_value);
    lssj_dict = {"xaxis": [],
                 "good_cover": [],
                 "bad_cover": [],
                 "call_success": [],
                 "ul_speed": [],
                 "dl_speed": [],
                 "dou": [],
                 "arpu": [],
                 "export_table": {},
                 };
    rounds = RoundsLog.objects.filter();
    lssj_table_1 = [];  # lssj_table是历史数据尾部表格的数据
    telphone = [];
    for ronud_item in rounds:
        telphone.append(get_value);
    lssj_dict["xaxis"] = RONUD_LIST;
    try:
        cover_list = UsrCoverPecpt.objects.filter(msisdn=get_value, rounds__in=RONUD_LIST[-6:]);
    except ValueError:
        pass
    except UsrCoverPecpt.DoesNotExist:
        pass;
    else:
        good_cover = [];
        bad_cover = [];
        cover_table_list = [];
        rsrp_list = [];
        bad_phr_list = [];
        for cover in cover_list:
            try:
                good_cover.append(cover.sum_point - cover.weak_point);
                bad_cover.append(cover.weak_point);
                cover_table_list.append(round((1 - cover.weak_point / cover.sum_point) * 100));
            except TypeError:
                good_cover.append(0);
                bad_cover.append(0);
                cover_table_list.append(0);
            try:
                rsrp_list.append(cover.avg_rsrp - 140);
                bad_phr_list.append(cover.bad_phr_rate);
            except:
                rsrp_list.append(None);
                bad_phr_list.append(None);

        lssj_dict["good_cover"] = good_cover;
        lssj_dict["bad_cover"] = bad_cover;
    # 查询用户常驻基站
    try:
        resident_list = UsrResidentCell.objects.filter(msisdn=get_value);
    except ValueError:
        pass
    except UsrResidentCell.DoesNotExist:
        pass;
    else:
        resident_l = [];
        user_enodeb = []
        for resident in resident_list:
            resident_l.append(resident.enodeb_id);
        cell_list = CellParaTable.objects.filter(enodeb_id__in=resident_l).values('enodeb_name').distinct();
        print(cell_list);
        # cell_list=CellParaTable.objects.distinct(enodeb_id__in=resident_l);
        for cell in cell_list:
            user_enodeb.append(cell["enodeb_name"]);
        while user_enodeb.__len__() < RONUD_LIST.__len__():
            user_enodeb.append(user_enodeb[-1]);

    # 用户通话信息
    try:
        call_list = UsrCallPecpt.objects.filter(msisdn=get_value, rounds__in=RONUD_LIST[-6:]);
    except ValueError:
        pass
    except UsrCallPecpt.DoesNotExist:
        pass;
    else:
        call_l = [];
        page_list = [];
        dc_list = [];
        for call in call_list:
            page_list.append(round(call.paging_rate, 2));
            dc_list.append(round(call.dc_rate, 2));
            call_l.append(round(call.paging_rate * (1 - call.dc_rate) / 100, 2)*100);
        lssj_dict["call_success"] = call_l;
        # 寻呼成功率,掉话率
    # 用户速率情况
    try:
        speed_list = UsrSpeedPecpt.objects.filter(msisdn=get_value, rounds__in=RONUD_LIST[-6:]);
    except ValueError:
        pass
    except UsrSpeedPecpt.DoesNotExist:
        pass;
    else:
        ul_speed_l = [];
        dl_speed_l = [];
        bp_ul = [];
        bp_dl = [];

        for speed in speed_list:
            ul_speed_l.append(speed.ul_speed);
            dl_speed_l.append(speed.dl_speed);
            bp_ul.append(speed.bp_ul_speed);
            bp_dl.append(speed.bp_dl_speed);
        lssj_dict["ul_speed"] = ul_speed_l;
        lssj_dict["dl_speed"] = dl_speed_l;

        # 用户消费情况
        try:
            expense_list = UsrExpenses.objects.filter(msisdn=get_value, rounds__in=RONUD_LIST[-6:]);
        except ValueError:
            pass
        except UsrExpenses.DoesNotExist:
            pass;
        else:
            dou_l = [];
            arpu_l = [];
            for expense in expense_list:
                dou_l.append(expense.last3m_avg_dou);
                arpu_l.append(expense.last3m_avg_arpu);
            lssj_dict["dou"] = dou_l;
            lssj_dict["arpu"] = arpu_l;

    # 核心网感知
    try:
        ete_list = UsrEtePecpt.objects.filter(msisdn=get_value, rounds__in=RONUD_LIST[-6:]);
    except ValueError:
        pass;
    except UsrEtePecpt.DoesNotExist:
        pass;
    else:
        http_list = [];
        tcpcgl_list = [];
        tcpsy_list = [];
        tcpwxcgl_list = [];
        tcpwxsy_list = [];
        ymxysy_list = [];
        for ete in ete_list:
            http_list.append(ete.http_res_rate);
            tcpcgl_list.append(ete.tcp_core_rate);
            tcpsy_list.append(ete.tcp_core_delay);
            tcpwxcgl_list.append(ete.tcp_radio_rate);
            tcpwxsy_list.append(ete.tcp_radio_delay);
            ymxysy_list.append(ete.page_res_delay);
    # 核心网数据
    try:
        core_list = UsrCorePecpt.objects.filter(msisdn=get_value, rounds__in=RONUD_LIST[-6:]);
    except ValueError:
        pass
    except UsrCorePecpt.DoesNotExist:
        pass;
    else:
        qhcgl_list = [];
        fwqqcgl_list = [];
        fzcgl_list = [];
        tau_list = [];
        for core in core_list:
            qhcgl_list.append(core.ho_rate);
            fwqqcgl_list.append(core.sr_rate);
            fzcgl_list.append(core.attach_rate);
            tau_list.append(core.tau_rate);
    # lssj_table表示使用{row0：[各个数据]}，的形式表示各行的数据,顺序不能乱了
    print(locals());
    lssj_table_1.append(RONUD_LIST);
    lssj_table_1.append(telphone);
    lssj_table_1.append(user_enodeb);
    lssj_table_1.append(cover_table_list);
    lssj_table_1.append(rsrp_list);
    lssj_table_1.append(bad_phr_list);
    lssj_table_1.append(page_list);
    lssj_table_1.append(dc_list);
    lssj_table_1.append(ul_speed_l);
    lssj_table_1.append(dl_speed_l);
    lssj_table_1.append(bp_ul);
    lssj_table_1.append(bp_dl);
    lssj_table_1.append(http_list);
    lssj_table_1.append(tcpcgl_list);
    lssj_table_1.append(tcpsy_list);
    lssj_table_1.append(tcpwxcgl_list);
    lssj_table_1.append(tcpwxsy_list);
    lssj_table_1.append(ymxysy_list);
    lssj_table_1.append(qhcgl_list);
    lssj_table_1.append(fwqqcgl_list);
    lssj_table_1.append(fzcgl_list);
    lssj_table_1.append(tau_list);

    lssj_table = transpose(lssj_table_1).tolist();
    lssj_table_dict = {};
    i = 0;
    while i < lssj_table.__len__():
        lssj_table_dict.update({"row" + str(i): lssj_table[i]});
        i += 1;
    lssj_table_dict.update({"length": lssj_table.__len__(), "attr_count": lssj_table[0].__len__()});
    lssj_dict["export_table"] = lssj_table_dict;
    lssj_dict.update(dict_user_basic);
    # 返回lssj_dict
    return lssj_dict;

def scpg_db_search(get_value):
    user_basic_info_dict = user_basic_info(get_value);
    # 查询用户app数据
    scpg_dict = {
        "app": "该数据缺失",
        "arpu": "该数据缺失",
        "dou": "该数据缺失",
        "call_time": "该数据缺失",
        "ztcmc": "该数据缺失",  # 主套餐名称
        "lldy500M": "该数据缺失",  # 流量大于500M用户
        "xykh": "该数据缺失",  # 校园客户
        "ctcyh": "该数据缺失",  # 超套餐用户
        "yjarpu": "该数据缺失",  # 月均arpu
        "qarpuyh": "该数据缺失",  # 前30%arpu用户
        "yjdou": "该数据缺失",  # 月均dou
        "doupm": "该数据缺失",  # dou排名
        "zdpp": "该数据缺失",  # 终端品牌
        "zdxh": "该数据缺失",  # 终端型号
        "lwyj": "该数据缺失",  # 离网预警用户
        "tsyh": "该数据缺失",  # 投诉用户
        "bmyyh": "该数据缺失",  # 不满意用户
    };
    try:
        single_UsrAppRank = UsrAppRank.objects.get(msisdn=get_value, rounds=RECENT_ROUND);
    except ValueError:
        pass
    except UsrAppRank.DoesNotExist:
        pass;
    else:
        scpg_dict["app"] = [{"name": single_UsrAppRank.top1_app_name, "value": single_UsrAppRank.top1_data, },
                            {"name": single_UsrAppRank.top2_app_name, "value": single_UsrAppRank.top2_data, },
                            {"name": single_UsrAppRank.top3_app_name, "value": single_UsrAppRank.top3_data, },
                            {"name": single_UsrAppRank.top4_app_name, "value": single_UsrAppRank.top4_data, },
                            {"name": single_UsrAppRank.top5_app_name, "value": single_UsrAppRank.top5_data, }, ],
        print(scpg_dict["app"]);
    # arpu,dou查询
    try:
        single_UsrExpenses = UsrExpenses.objects.get(msisdn=get_value, rounds=RECENT_ROUND);
    except ValueError:
        pass
    except UsrExpenses.DoesNotExist:
        pass;
    else:
        scpg_dict["arpu"] = [single_UsrExpenses.last3m_avg_arpu / 500];
        scpg_dict["dou"] = [single_UsrExpenses.last3m_avg_dou / 30000];
        scpg_dict["call_time"] = "3000min";
        scpg_dict["ztcmc"] = single_UsrExpenses.packages_name;
        scpg_dict["lldy500M"] = single_UsrExpenses.up_500m_user;
        if single_UsrExpenses.college_user == 1:
            scpg_dict["xykh"] = "是";
        else:
            scpg_dict["xykh"] = "否";
        scpg_dict["ctcyh"] = single_UsrExpenses.over_packges_user;
        scpg_dict["yjarpu"] = single_UsrExpenses.last3m_avg_arpu;
        if single_UsrExpenses.if_30_arpu == 1:
            scpg_dict["qarpuyh"] = "是";
        else:
            scpg_dict["qarpuyh"] = "否";
        scpg_dict["yjdou"] = single_UsrExpenses.last3m_avg_dou;
        if single_UsrExpenses.if_30_dou == 1:
            scpg_dict["doupm"] = "是";
        else:
            scpg_dict["doupm"] = "否";
        scpg_dict["zdpp"] = user_basic_info_dict["phone_brand"];
        scpg_dict["zdxh"] = user_basic_info_dict["phone_type"];
        scpg_dict["lwyj"] = user_basic_info_dict["is_risk_user"];
        scpg_dict["tsyh"] = user_basic_info_dict["is_complaint_user"];
        scpg_dict["bmyyh"] = user_basic_info_dict["is_discontent_user"];
    scpg_dict.update(user_basic_info_dict);
    return scpg_dict;

def yhty_db_search(get_value):
    user_basic_info_dict = user_basic_info(get_value);
    yhty_dict = {
        "round": [],
        "avg_score": 0,
        "data": [],
    };
    try:
        score_list = UsrScoreReturn.objects.filter(msisdn=get_value, rounds__in=RONUD_LIST);
    except ValueError:
        pass;
    except UsrScoreReturn.DoesNotExist:
        pass;
    else:
        i = 0;
        while i < score_list.__len__():
            yhty_dict["data"].append({"name": RONUD_LIST[i],
                                      "value": [round(score_list[i].score_usr_worth,2),
                                                round(score_list[i].score_usr_cover_pecpt,2),
                                                round(score_list[i].score_usr_speed_pecpt,2),
                                                round(score_list[i].score_usr_ete_pecpt,2),
                                                round(score_list[i].score_usr_sensitivity,2)]})
            i += 1;
    yhty_dict["round"] = RONUD_LIST;
    try:
        yhty_dict["avg_score"] = round((score_list[i-1].score_usr_worth + score_list[i-1].score_usr_cover_pecpt + \
                                        score_list[i-1].score_usr_speed_pecpt + score_list[i-1].score_usr_ete_pecpt + score_list[i-1].score_usr_sensitivity) / 5);
    except:
        yhty_dict["avg_score"] = 0;
    yhty_dict.update(user_basic_info_dict);
    return yhty_dict;