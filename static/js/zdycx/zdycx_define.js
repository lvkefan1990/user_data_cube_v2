
//定义元素,首先定义checkbox
var user_basic_checkbox = document.getElementById("user_basic_checkbox");

//定义div
var basic_condition_div = document.getElementById("user_basic_div");

//定义列表
var city_select = document.getElementById("city_select");
var district_select = document.getElementById("district_select");//获取第二个下拉列表对象
var district_all = document.getElementById("district_all");
var condition_ul = document.getElementById("condition_ul");//条件集合
var column_ul = document.getElementById("column_ul");//结果集合

//定义所要导出的表
var export_table = document.getElementById("export_table");
var export_table_thead = document.getElementById("export_table_thead");
var export_table_tbody = document.getElementById("export_table_tbody");

//定义条件的json数据的格式，用于显示条件集合和发送json数据
var condition_list=['接通率','掉话率','全业务下行速率','大包下行速率','全业务上行速率','大包上行速率','HTTP响应成功率',
'TCP核心网成功率','TCP重传率','差RIP率','切换成功率','服务请求成功率','附着成功率','PDN连接成功率','INITIAL成功率','TAU成功率',
'平均RSRP','MR覆盖率','脱网率','差PHR率','是否500M以上流量或套餐订购用户','超套餐流量客户','前30%ARPU用户','前30%DOU值用户',
'是否离网预警','是否投诉用户','是否不满意用户','是否校园客户','是否超套餐流量客户'];

//定义查询按钮向后台发出请求的json数据
var zdycx_json={
    condition:{
    "地市":"",
    "区县":[],
    "起始时间":"",
    "终止时间":"",
    },
    result:['地市','区县','起始时间','终止时间','电话号码'],
    change:0,
}
