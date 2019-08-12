// 定义函数，处理元素的innerText属性存在的浏览器兼容性
function writeText(element,content){
    if(typeof(element.innerText) === 'string'){
        element.innerText=content;
    }else{
        element.textContent=content;
    }
}
 //定义用户基础表格
var phonenumber_td = document.getElementById('phonenumber');
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
var portrait = echarts.init(document.getElementById('portrait'),'dark');
var pjdf_f = document.getElementById('pjdf_f');

//定义按钮
var search = document.getElementById('search');

