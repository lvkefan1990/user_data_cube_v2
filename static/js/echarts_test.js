// 定义函数，处理元素的innerText属性存在的浏览器兼容性
function writeText(element,content){
    if(typeof(element.innerText) === 'string'){
        element.innerText=content;
    }else{
        element.textContent=content;
    }
}
// 使用刚指定的配置项和数据显示图表。
//定义图表
var cover = echarts.init(document.getElementById('coverage'));
var rsrp = echarts.init(document.getElementById('rsrp'));
var app = echarts.init(document.getElementById('app'));
var dl_speed = echarts.init(document.getElementById('dl_speed'));
var call_success = echarts.init(document.getElementById('call_success'));
var arpu = echarts.init(document.getElementById('arpu'));
var dou = echarts.init(document.getElementById('dou'));
var call_time = echarts.init(document.getElementById('call_time'));
var portrait = echarts.init(document.getElementById('portrait'));

//提交
function single_user_ph_submit(){
        var phone_number=document.getElementById("phone_number").value;
        var xhr;
        if(window.XMLHttpRequest){
            xhr= new XMLHttpRequest();
        }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
        xhr.open(methon="POST",url='/single_user_ph_submit/',async=true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange=function () {
            if(xhr.readyState == 4&& xhr.status == 200){
                single_user_json= JSON.parse(xhr.responseText);
                writeText(phonemuber_td,single_user_json.phonemuber);
                writeText(city_td,single_user_json.user_city);
                writeText(district_td,single_user_json.district);
                writeText(county_td,single_user_json.county);
                writeText(citizen_or_villager_td,single_user_json.citizen_or_villager);
                writeText(star_td,single_user_json.star);
                writeText(begin_td,single_user_json.begin);
                writeText(length_of_time_td,single_user_json.length_of_time);
                //writeText(phone_city_td,single_user_json.begin);
                writeText(phone_brand_td,single_user_json.phone_brand);
                writeText(phone_type_td,single_user_json.phone_type);
                //writeText(user_address_td,single_user_json.phone_type);
                //表格完成，phone_city和user_address可以用投诉记录代替,接下来将设计图形选项

            } else{
                //alert(xhr.status);
            }
            };
        xhr.send('phone_number='+phone_number)
    }