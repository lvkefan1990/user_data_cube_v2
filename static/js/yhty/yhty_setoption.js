function chaxun() {
        writeText(pjdf_f,"");
        var now_time=new Date;
        var time=now_time.getFullYear().toString()+"年"+(now_time.getMonth()+1).toString()+"月"+now_time.getDate().toString()+"日";
        //+ now_time.getHours()+"时"+now_time.getMinutes()+"分";
        var phone_number = document.getElementById("phone_number").value;
        var xhr;
        if(window.XMLHttpRequest){
            xhr= new XMLHttpRequest();
        }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
        xhr.open(methon="POST",url='/yhty_submit/',async=true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange=function () {
            if(xhr.readyState == 4){
            $("#search").attr("disabled",false).css("pointer-events","auto");
                if(xhr.status == 200){
                yhty_obj= JSON.parse(xhr.responseText);
                if (yhty_obj.error_text == "正常"){
                    writeText(error_td,"");
                    writeText(phonenumber_td,yhty_obj.phonemuber);
                    writeText(city_td,yhty_obj.user_city);
                    writeText(district_td,yhty_obj.district);
                    writeText(county_td,yhty_obj.county);
                    writeText(citizen_or_villager_td,yhty_obj.citizen_or_villager);
                    writeText(star_td,yhty_obj.star);
                    writeText(begin_td,yhty_obj.begin);
                    writeText(length_of_time_td,yhty_obj.length_of_time);
                    writeText(phone_brand_td,yhty_obj.phone_brand);
                    writeText(is_header_user_td,yhty_obj.is_header_user);
                    writeText(is_risk_user_td,yhty_obj.is_risk_user);
                    writeText(phone_type_td,yhty_obj.phone_type);
                    portrait_option.legend.data=yhty_obj.round;
                    portrait_option.series.data=yhty_obj.data;
                    portrait.setOption(portrait_option);
                    writeText(pjdf_f,yhty_obj.avg_score);
                }
                else{
                    writeText(error_td,yhty_obj.error_text);
                    writeText(phonenumber_td,"");
                    writeText(city_td,"");
                    writeText(district_td,"");
                    writeText(county_td,"");
                    writeText(citizen_or_villager_td,"");
                    writeText(star_td,"");
                    writeText(begin_td,"");
                    writeText(length_of_time_td,"");
                    writeText(phone_brand_td,"");
                    writeText(is_header_user_td,"");
                    writeText(is_risk_user_td,"");
                    writeText(phone_type_td,"");
                    portrait.clear();
                    writeText(pjdf_f,"");
                }
            }
    }}
        xhr.send('phone_number='+phone_number);
        $("#search").attr("disabled",true).css("pointer-events","none");
}
//用户体验onload事件
function yhty_onload() {
        writeText(pjdf_f,"");
        var now_time=new Date;
        var time=now_time.getFullYear().toString()+"年"+(now_time.getMonth()+1).toString()+"月"+now_time.getDate().toString()+"日";
        //+ now_time.getHours()+"时"+now_time.getMinutes()+"分";
        var xhr;
        if(window.XMLHttpRequest){
            xhr= new XMLHttpRequest();
        }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
        xhr.open(methon="POST",url='/yhty_onload/',async=true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange=function () {
            if(xhr.readyState == 4){
                $("#search").attr("disabled",false).css("pointer-events","auto");
                if(xhr.status == 200){
                    yhty_obj= JSON.parse(xhr.responseText);
                    if(yhty_obj.error_text == "正常" && yhty_obj.phonemuber != ""){
                    writeText(error_td,"");
                    writeText(phonenumber_td,yhty_obj.phonemuber);
                    writeText(city_td,yhty_obj.user_city);
                    writeText(district_td,yhty_obj.district);
                    writeText(county_td,yhty_obj.county);
                    writeText(citizen_or_villager_td,yhty_obj.citizen_or_villager);
                    writeText(star_td,yhty_obj.star);
                    writeText(begin_td,yhty_obj.begin);
                    writeText(length_of_time_td,yhty_obj.length_of_time);
                    writeText(phone_brand_td,yhty_obj.phone_brand);
                    writeText(is_header_user_td,yhty_obj.is_header_user);
                    writeText(is_risk_user_td,yhty_obj.is_risk_user);
                    writeText(phone_type_td,yhty_obj.phone_type);
                    portrait_option.legend.data=yhty_obj.round;
                    portrait_option.series.data=yhty_obj.data;
                    portrait.setOption(portrait_option);
                    writeText(pjdf_f,yhty_obj.avg_score);
                }}
            }}
        xhr.send();
        $("#search").attr("disabled",true).css("pointer-events","none");
    }

