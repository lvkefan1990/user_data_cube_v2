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
var lssj_echarts = echarts.init(document.getElementById('lssj_echarts'),"dark");

//定义选项卡
var fggz_li = document.getElementById('fggz_li');
var thgz_li = document.getElementById('thgz_li');
var slgz_li = document.getElementById('slgz_li');
var zfnl_li = document.getElementById('zfnl_li');

//定义导出的表
var lssj_table = document.getElementById('lssj_table');
var lssj_table_tbody=document.getElementById('lssj_table_tbody');
//定义导出按钮
var lssj_export = document.getElementById('lssj_table');