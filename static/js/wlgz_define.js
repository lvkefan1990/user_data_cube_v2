// 定义函数，处理元素的innerText属性存在的浏览器兼容性
function writeText(element,content){
    if(typeof(element.innerText) === 'string'){
        element.innerText=content;
    }else{
        element.textContent=content;
    }
}
 //定义用户基础表格
var phonemuber_td = document.getElementById('phonemuber');
var city_td = document.getElementById('city');
var district_td = document.getElementById('district');
var county_td = document.getElementById('county');
var citizen_or_villager_td = document.getElementById('citizen_or_villager');
var star_td = document.getElementById('star');
var begin_td = document.getElementById('begin');
var length_of_time_td = document.getElementById('length_of_time');
var belong_td = document.getElementById('belong');
var phone_brand_td = document.getElementById('phone_brand');
var is_header_user_td = document.getElementById('is_header_user');
var is_risk_user_td = document.getElementById('is_risk_user');
var phone_type_td = document.getElementById('phone_type');
var error_td = document.getElementById('error');

//定义图表
var cover = echarts.init(document.getElementById('coverage'),"dark");
var rsrp = echarts.init(document.getElementById('rsrp'),"dark");
var dl_speed = echarts.init(document.getElementById('dl_speed'),"dark");
var call_success = echarts.init(document.getElementById('call_success'),"dark");
//var app = echarts.init(document.getElementById('app'));
//var apu = echarts.init(document.getElementById('apu'));
//var dou = echarts.init(document.getElementById('dou'));
//var call_time = echarts.init(document.getElementById('call_time'));
//var portrait = echarts.init(document.getElementById('portrait'));

//定义查询结果表格
var date_td = document.getElementById('date');
var yhdh_td = document.getElementById('yhdh');
var yhczxq_td = document.getElementById('yhczxq');
var fgl_td = document.getElementById('fgl');
var pjrsrp_td = document.getElementById('pjrsrp');
var cphrl_td = document.getElementById('cphrl');
var xhcgl_td = document.getElementById('xhcgl');
var dxl_td = document.getElementById('dxl');
var qywsxsl_td = document.getElementById('qywsxsl');
var qywxxsl_td = document.getElementById('qywxxsl');
//var dbsxsl_td = document.getElementById('dbsxsl');
//var dbxxsl_td = document.getElementById('dbxxsl');
var http_td = document.getElementById('http');
var tcpcgl_td = document.getElementById('tcpcgl');
var tcpsy_td = document.getElementById('tcpsy');
var tcpwxcgl_td = document.getElementById('tcpwxcgl');
var tcpwxsy_td = document.getElementById('tcpwxsy');
var ymxysy_td = document.getElementById('ymxysy');
var qhcgl_td = document.getElementById('qhcgl');
var fwqqcgl_td = document.getElementById('fwqqcgl');
var fzcgl_td = document.getElementById('fzcgl');
var tau_td = document.getElementById('tau');
