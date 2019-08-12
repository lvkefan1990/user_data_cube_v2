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

 //定义市场echarts图表
var app = echarts.init(document.getElementById('app'),"dark");
var apru = echarts.init(document.getElementById('apru'),"dark");
var dou = echarts.init(document.getElementById('dou'),"dark");
var call_time = document.getElementById('call_time');

//定义查询结果表格
var date_td = document.getElementById('date');
var yhdh_td = document.getElementById('yhdh');
var ztcmc_td = document.getElementById('ztcmc');
var lldy500M_td = document.getElementById('lldy500M');
var xykh_td = document.getElementById('xykh');
var ctcyh_td = document.getElementById('ctcyh');
var yjarpu_td = document.getElementById('yjarpu');
var qarpuyh_td = document.getElementById('qarpuyh');
var yjdou_td = document.getElementById('yjdou');
var doupm_td = document.getElementById('doupm');
var zdpp_td = document.getElementById('zdpp');
var zdxh_td = document.getElementById('zdxh');
var lwyj_td = document.getElementById('lwyj');
var tsyh_td = document.getElementById('tsyh');
var bmyyh_td = document.getElementById('bmyyh');

//定义按钮
var search = document.getElementById('search');
