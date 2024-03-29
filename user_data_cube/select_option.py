# 表：表名
table={
    "用户用户基础信息表": "usr_basic_info",
    "用户常驻小区表": "usr_resident_cell",
    "用户APP排名表": "usr_app_rank",
    "用户通话感知表": "usr_call_pecpt",
    "用户APP速率表": "usr_app_pecpt",
    "用户上网速率表": "usr_speed_pecpt",
    "用户端到端感知表": "usr_ete_pecpt",
    "用户核心网感知表": "usr_core_pecpt",
    "用户覆盖感知表": "usr_cover_pecpt",
    "用户消费行为表": "usr_expenses",
    "用户终端关系表": "tac_imei_relation",
    "用户投诉记录表": "usr_complt_record",
};
#字段：字段名
user_data_cube_fleld = {
    "地市":"usr_basic_info.CITY",
    "区县":"usr_basic_info.AREA",
    "电话号码":"usr_basic_info.MSISDN",
    "星级":"usr_basic_info.STAR_TYPE",
    "营业部":"usr_basic_info.AREA1",
    "农村城市属性":"usr_basic_info.OVERLAY_AREA",
    "开户时间":"usr_basic_info.START_DATE",
    "在网时长":"usr_basic_info.ONLINE_TIME",
    "基站ID":"usr_resident_cell.ENODEB_ID",
    "用户常驻基站":"usr_resident_cell.ENODEB_NAME",
    "TOP1APP名称":"usr_app_rank.TOP1_APP_NAME",
    "TOP1APP流量":"usr_app_rank.TOP1_DATA",
    "TOP1APP点击量":"usr_app_rank.TOP1_SESSION",
    "TOP2APP名称":"usr_app_rank.TOP2_APP_NAME",
    "TOP2APP流量":"usr_app_rank.TOP2_DATA",
    "TOP2APP点击量":"usr_app_rank.TOP2_SESSION",
    "TOP3APP名称":"usr_app_rank.TOP3_APP_NAME",
    "TOP3APP流量":"usr_app_rank.TOP3_DATA",
    "TOP3APP点击量":"usr_app_rank.TOP3_SESSION",
    "TOP4APP名称":"usr_app_rank.TOP4_APP_NAME",
    "TOP4APP流量":"usr_app_rank.TOP4_DATA",
    "TOP4APP点击量":"usr_app_rank.TOP4_SESSION",
    "TOP5APP名称":"usr_app_rank.TOP5_APP_NAME",
    "TOP5APP流量":"usr_app_rank.TOP5_DATA",
    "TOP5APP点击量":"usr_app_rank.TOP5_SESSION",
    "接通率": "usr_call_pecpt.PAGING_RATE",
    "掉话率": "usr_call_pecpt.DC_RATE",
    "APP感知TOP1APP名称": "usr_app_pecpt.TOP1_APP_NAME",
    "APP感知TOP1APP小包时延": "usr_app_pecpt.TOP1_SP_DELAY",
    "APP感知TOP1APP_B1速率": "usr_app_pecpt.TOP1_B1_SPEED",
    "APP感知TOP1APP_B2速率": "usr_app_pecpt.TOP1_B2_SPEED",
    "APP感知TOP1APP_B3速率": "usr_app_pecpt.TOP1_B3_SPEED",
    "APP感知TOP2APP名称": "usr_app_pecpt.TOP2_APP_NAME",
    "APP感知TOP2APP小包时延": "usr_app_pecpt.TOP2_SP_DELAY",
    "APP感知TOP2APP_B1速率": "usr_app_pecpt.TOP2_B1_SPEED",
    "APP感知TOP2APP_B2速率": "usr_app_pecpt.TOP2_B2_SPEED",
    "APP感知TOP2APP_B3速率": "usr_app_pecpt.TOP2_B3_SPEED",
    "APP感知TOP3APP名称": "usr_app_pecpt.TOP3_APP_NAME",
    "APP感知TOP3APP小包时延": "usr_app_pecpt.TOP3_SP_DELAY",
    "APP感知TOP3APP_B1速率": "usr_app_pecpt.TOP3_B1_SPEED",
    "APP感知TOP3APP_B2速率": "usr_app_pecpt.TOP3_B2_SPEED",
    "APP感知TOP3APP_B3速率": "usr_app_pecpt.TOP3_B3_SPEED",
    "APP感知TOP4APP名称": "usr_app_pecpt.TOP4_APP_NAME",
    "APP感知TOP4APP小包时延": "usr_app_pecpt.TOP4_SP_DELAY",
    "APP感知TOP4APP_B1速率": "usr_app_pecpt.TOP4_B1_SPEED",
    "APP感知TOP4APP_B2速率": "usr_app_pecpt.TOP4_B2_SPEED",
    "APP感知TOP4APP_B3速率": "usr_app_pecpt.TOP4_B3_SPEED",
    "APP感知TOP5APP名称": "usr_app_pecpt.TOP5_APP_NAME",
    "APP感知TOP5APP小包时延": "usr_app_pecpt.TOP5_SP_DELAY",
    "APP感知TOP5APP_B1速率": "usr_app_pecpt.TOP5_B1_SPEED",
    "APP感知TOP5APP_B2速率": "usr_app_pecpt.TOP5_B2_SPEED",
    "APP感知TOP5APP_B3速率": "usr_app_pecpt.TOP5_B3_SPEED",
    "全业务下行速率": "usr_speed_pecpt.DL_SPEED",
    "大包下行速率": "usr_speed_pecpt.BP_DL_SPEED",
    "大包下行流量": "usr_speed_pecpt.BP_DL_DATA",
    "大包下行时长": "usr_speed_pecpt.BP_DL_DURA",
    "全业务上行速率": "usr_speed_pecpt.UL_SPEED",
    "大包上行速率": "usr_speed_pecpt.BP_UL_SPEED",
    "小包下行时延": "usr_speed_pecpt.SP_DL_DELAY",
    "小包上行时延": "usr_speed_pecpt.SP_UL_DELAY",
    "HTTP响应成功率": "usr_ete_pecpt.HTTP_RES_RATE",
    "HTTP请求次数": "usr_ete_pecpt.HTTP_ATT",
    "HTTP响应时延": "usr_ete_pecpt.HTTP_RES_DELAY",
    "TCP核心网成功率": "usr_ete_pecpt.TCP_CORE_RATE",
    "TCP核心网时延": "usr_ete_pecpt.TCP_CORE_DELAY",
    "TCP无线时延": "usr_ete_pecpt.TCP_RADIO_DELAY",
    "TCP下行重传率": "usr_ete_pecpt.TCP_DL_RE_RATE",
    "TCP上行重传率": "usr_ete_pecpt.TCP_UL_RE_RATE",
    "TCP重传率": "usr_ete_pecpt.TCP_RE_RATE",
    "页面响应时延": "usr_ete_pecpt.PAGE_RES_DELAY",
    "页面响应次数": "usr_ete_pecpt.PAGE_RES_SESSION",
    "差RIP率": "usr_core_pecpt.BAD_RIP_RATE",
    "切换成功率": "usr_core_pecpt.HO_RATE",
    "服务请求成功率": "usr_core_pecpt.SR_RATE",
    "附着成功率": "usr_core_pecpt.ATTACH_RATE",
    "PDN连接成功率": "usr_core_pecpt.PDN_RATE",
    "INITIAL成功率": "usr_core_pecpt.INITIAL_RATE",
    "TAU成功率": "usr_core_pecpt.TAU_RATE",
    "MR采样点": "usr_cover_pecpt.SUM_POINT",
    "MR弱采样点": "usr_cover_pecpt.POOR_POINT",
    "低于-100的采样点": "usr_cover_pecpt.WEAK_POINT",
    "平均RSRP": "usr_cover_pecpt.AVG_RSRP",
    "MR_RATE_100": "usr_cover_pecpt.MR_RATE_100",
    "MR覆盖率": "usr_cover_pecpt.MR_RATE",
    "脱网率": "usr_cover_pecpt.OFF_RATE",
    "差PHR率": "usr_cover_pecpt.BAD_PHR_RATE",
    "主套餐名称": "usr_expenses.PACKAGES_NAME",
    "是否500M以上流量或套餐订购用户": "usr_expenses.UP_500M_USER",
    "主套餐加附加套餐包含流量": "usr_expenses.FLOWS",
    "超套餐流量客户": "usr_expenses.OVER_PACKGES_USER",
    "近三个月月均ARPU": "usr_expenses.LAST3M_AVG_ARPU",
    "ARPU排名": "usr_expenses.ARPU_RANK",
    "前30%ARPU用户": "usr_expenses.IF_30_ARPU",
    "近三个月月均DOU": "usr_expenses.LAST3M_AVG_DOU",
    "DOU排名": "usr_expenses.DOU_RANK",
    "前30%DOU值用户": "usr_expenses.IF_30_DOU",
    "终端品牌": "tac_imei_relation.BRAND",
    "终端型号": "tac_imei_relation.TYPE",
    "是否离网预警": "usr_complt_record.IF_RISK_USER",
    "离网预警归因": "usr_complt_record.POLICY_PRODUCT",
    "是否投诉用户": "usr_complt_record.POLICY_PRODUCT",
    "投诉原因1": "usr_complt_record.REASON1",
    "投诉原因2": "usr_complt_record.REASON2",
    "投诉业务": "usr_complt_record.BUSINESS",
    "是否不满意用户": "usr_complt_record.IF_DISCONTENT_USER",
    "不满意原因": "usr_complt_record.RFD",
    "维系措施": "usr_complt_record.DFW",
    "是否校园客户": "usr_complt_record.COLLEGE_USR",
    "是否超套餐流量客户": "usr_complt_record.OVER_PACKGES_USER",
    };

yes_or_no={
    "是":"('1','是')",
    "否":"('0','否')"
};

#去除重复项
def unique(list=[]):
    list_l = [];
    for l in list:
        if l not in list_l:
            list_l.append(l);
    return list_l;

