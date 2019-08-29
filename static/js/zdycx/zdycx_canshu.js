//一些元素的id的列表，在显示隐藏函数中使用
//基础用户信息的显示和隐藏
var usr_basic_info_xianshi = ['usr_basic_info_title','usr_resident_cell_title'];
var usr_basic_info_yincang = ['usr_basic_info_title','usr_resident_cell_title','usr_basic_info','usr_resident_cell'];

//用户常驻基站的显示和隐藏
var usr_basic_info_table_xianshi=['usr_basic_info'];
var usr_basic_info_table_yincang=['usr_basic_info'];

//用户常驻基站的显示和隐藏
var usr_resident_cell_xianshi=['usr_resident_cell'];
var usr_resident_cell_yincang=['usr_resident_cell'];

//用户上网行为的显示和隐藏
var user_netbehavior_xianshi =['usr_app_rank_title'];
var user_netbehavior_yincang =['usr_app_rank_title','usr_app_rank'];

//用户APP排名表显示和隐藏
var usr_app_rank_xianshi=['usr_app_rank'];
var usr_app_rank_yincang=['usr_app_rank'];

//用户网络感知显示和隐藏
var user_netpecpt_xianshi=['usr_call_pecpt_title','usr_app_pecpt_title','usr_speed_pecpt_title',
    'usr_ete_pecpt_title','usr_core_pecpt_title','usr_cover_pecpt_title'];
var user_netpecpt_yincang=['usr_call_pecpt_title','usr_app_pecpt_title','usr_speed_pecpt_title', 'usr_ete_pecpt_title',
    'usr_core_pecpt_title','usr_cover_pecpt_title','usr_call_pecpt','usr_app_pecpt','usr_speed_pecpt','usr_ete_pecpt',
    'usr_core_pecpt','usr_cover_pecpt'];

//用户通话感知表显示和隐藏
var usr_call_pecpt_xianshi = ['usr_call_pecpt'];
var usr_call_pecpt_yincang = ['usr_call_pecpt'];

//用户APP感知表显示和隐藏
var usr_app_pecpt_xianshi = ['usr_app_pecpt'];
var usr_app_pecpt_yincang = ['usr_app_pecpt'];

//用户上网速率表
var usr_speed_pecpt_xianshi = ['usr_speed_pecpt'];
var usr_speed_pecpt_yincang = ['usr_speed_pecpt'];

//用户端到端感知表
var usr_ete_pecpt_xianshi = ['usr_ete_pecpt'];
var usr_ete_pecpt_yincang = ['usr_ete_pecpt'];

//用户核心网感知表
var usr_core_pecpt_xianshi = ['usr_core_pecpt'];
var usr_core_pecpt_yincang = ['usr_core_pecpt'];

//用户覆盖表
var usr_cover_pecpt_xianshi =['usr_cover_pecpt'];
var usr_cover_pecpt_yincang =['usr_cover_pecpt'];

//用户消费行为显示和隐藏
var usr_expensesbehavior_xianshi =['usr_expenses_title'];
var usr_expensesbehavior_yincang = ['usr_expenses_title','usr_expenses'];

//用户消费行为表显示和隐藏
var usr_expenses_xianshi = ['usr_expenses'];
var usr_expenses_yincang = ['usr_expenses'];

//用户终端关系的显示和隐藏
var tac_imei_relation_xianshi = ['tac_imei_relation_title'];
var tac_imei_relation_yincang = ['tac_imei_relation_title','tac_imei_relation'];

//用户终端关系表显示和隐藏
var tac_imei_relation_table_xianshi = ['tac_imei_relation'];
var tac_imei_relation_table_yincang = ['tac_imei_relation'];

//用户投诉记录显示和隐藏
var usr_complt_record_xianshi = ['usr_complt_record_title'];
var usr_complt_record_yincang = ['usr_complt_record_title','usr_complt_record'];

//用户投诉记录表显示和隐藏
var usr_complt_record_table_xianshi = ['usr_complt_record'];
var usr_complt_record_table_yincang = ['usr_complt_record'];

//全选函数参数
var usr_call_pecpt_input = ['paging_rate_start','paging_rate_end','dc_rate_start','dc_rate_end'];
var usr_speed_pecpt_input = ["dl_speed_start","dl_speed_end","bp_dl_speed_start","bp_dl_speed_end","ul_speed_start","ul_speed_end",
    "bp_ul_speed_start","bp_ul_speed_end"];
var usr_ete_pecpt_input = ['http_res_rate_start','http_res_rate_end','tcp_core_rate_start','tcp_core_rate_end','tcp_radio_rate_start',
'tcp_radio_rate_end'];
var usr_core_pecpt_input =['bad_rip_rate_start','bad_rip_rate_end','ho_rate_start','ho_rate_end','sr_rate_start','sr_rate_end',
'attach_rate_start','attach_rate_end','pdn_rate_start','pdn_rate_end','initial_rate_start','initial_rate_end','tau_rate_start','tau_rate_end'];
var usr_cover_pecpt_input = ['avg_rsrp_start','avg_rsrp_end','mr_rate_start','mr_rate_end','off_rate_start','off_rate_end',
    'bad_phr_rate_start','bad_phr_rate_end'];

//将所有字段取名，组成一个名字列表
var attr_name_list=['usr_basic_info_attr','msisdn','usr_resident_cell_attr','usr_app_rank_attr','usr_call_pecpt_attr',
'usr_app_pecpt_attr','usr_speed_pecpt_attr','usr_ete_pecpt_attr','usr_core_pecpt_attr','usr_cover_pecpt_attr','usr_expenses_attr',
'tac_imei_relation_attr','usr_complt_record_attr'];





