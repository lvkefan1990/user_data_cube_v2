from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(UsrScoreReturn)
class UsrScoreReturnAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'score_usr_worth', 'score_usr_cover_pecpt',
                    'score_usr_speed_pecpt', 'score_usr_ete_pecpt', 'score_usr_sensitivity')
    #list_per_page设置每页要显示多少条记录，默认是100条
    list_per_page = 100
    #ordering设置默认排序字段，负号表示降序排列
    ordering = ('id',)
    #操作项显示位置功能设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    actions_on_bottom = False
    #操作项功能显示选中项的数目
    actions_selection_counter = True
    #字段为空值显示的内容
    #过滤器功能及能过滤的字段
    #list_filter = ('id',)
    #搜索功能及能实现搜索的字段
    search_fields = ('id',)

@admin.register(UsrSpeedPecpt)
class UsrSpeedPecptAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'dl_speed', 'bp_dl_speed',
                    'bp_dl_dura', 'ul_speed', 'sp_dl_delay', 'sp_ul_delay')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrResidentCell)
class UsrRsidentCellAdmin(admin.ModelAdmin):
    list_display = ('msisdn', 'enodeb_id')
    list_per_page = 100
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True

@admin.register(UsrExpenses)
class UsrExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'packages_name', 'up_500m_user', 'college_user',
                    'last3m_avg_arpu', 'arpu_rank', 'if_30_arpu', 'last3m_avg_dou', 'dou_rank', 'if_30_dou')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrEtePecpt)
class UsrEtePecpt(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'http_res_rate', 'http_att', 'http_res_delay',
                    'tcp_core_rate', 'tcp_core_delay', 'tcp_radio_rate', 'tcp_radio_delay', 'tcp_dl_re_rate',
                    'tcp_ul_re_rate', 'tcp_re_rate', 'page_res_delay', 'page_res_session')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrCoverPecpt)
class UsrCoverPecpt(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'sum_point', 'poor_point', 'weak_point',
                    'avg_rsrp', 'mr_rate_100', 'mr_rate', 'off_rate', 'bad_phr_rate')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrCorePecpt)
class UsrCorePecptAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'bad_rip_rate', 'ho_rate', 'sr_rate',
                    'attach_rate', 'pdn_rate', 'initial_rate', 'tau_rate')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrCompltRecord)
class UsrCompltRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'if_risk_user', 'policy_product', 'if_complaint_user',
                    'reason1', 'reason2', 'business', 'if_discontent_user', 'rfd', 'dfw', 'over_packges_user')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrCallPecpt)
class UsrCallPecptAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'paging_rate', 'dc_rate')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrBasicInfo)
class UsrBasicInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'city', 'area', 'area1', 'star_type', 'start_date',
                    'online_time')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrAppRank)
class UsrAppRankAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'top1_app_name', 'top1_session', 'top1_data',
                    'top2_app_name', 'top2_session', 'top2_data',
                    'top3_app_name', 'top3_session', 'top3_data',
                    'top4_app_name', 'top4_session', 'top4_data',
                    'top5_app_name', 'top5_session', 'top5_data')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(UsrAppPecpt)
class UsrAppPecptAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn',
                    'top1_app_name', 'top1_sp_delay', 'top1_b1_speed', 'top1_b2_speed', 'top1_b3_speed',
                    'top2_app_name', 'top2_sp_delay', 'top2_b1_speed', 'top2_b2_speed', 'top2_b3_speed',
                    'top3_app_name', 'top3_sp_delay', 'top3_b1_speed', 'top3_b2_speed', 'top3_b3_speed',
                    'top4_app_name', 'top4_sp_delay', 'top4_b1_speed', 'top4_b2_speed', 'top4_b3_speed',
                    'top5_app_name', 'top5_sp_delay', 'top5_b1_speed', 'top5_b2_speed', 'top5_b3_speed')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(TacImeiRelation)
class TacImeiRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'rounds', 'sdate', 'msisdn', 'brand', 'type')
    list_per_page = 100
    ordering = ('id',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('id',)

@admin.register(CellParaTable)
class CellParaTable(admin.ModelAdmin):
    list_display = ('cellid', 'sdate', 'enodeb_name', 'cell_name', 'enodeb_id', 'cell_id', 'factory',
                    'cover_type', 'cover_fomat', 'earfcn', 'pci', 'tac', 'mod3', 'mod3_group')
    list_per_page = 100
    ordering = ('cellid',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('enodeb_id', 'factory', 'enodeb_name',)

@admin.register(CellBasicInfo)
class CellBasicInfo(admin.ModelAdmin):
    list_display = ('cellid', 'sdate', 'area', 'local_area', 'enodeb_name', 'cell_name', 'cell_grid',
                    'longitude', 'latitude', 'azimuth')
    list_per_page = 100
    ordering = ('cellid',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('area', 'local_area', 'enodeb_name', 'cell_grid',)

@admin.register(UsrLogin)
class UsrLoginAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password')
    list_per_page = 100
    ordering = ('user_name',)
    actions_on_top = True
    actions_on_bottom = False
    actions_selection_counter = True
    search_fields = ('user_name', 'password',)

#在admin中注册对应的类模型
admin.site.site_header = '用户数据魔方后台管理'
admin.site.site_title = '用户数据魔方'