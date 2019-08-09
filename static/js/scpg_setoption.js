function chaxun() {
        var now_time=new Date;
        alert("good")
        var time=now_time.getFullYear().toString()+"年"+(now_time.getMonth()+1).toString()+"月"+now_time.getDate().toString()+"日";
        //+ now_time.getHours()+"时"+now_time.getMinutes()+"分";
        var phone_number = document.getElementById("phone_number").value;
        var xhr;
        if(window.XMLHttpRequest){
            xhr= new XMLHttpRequest();
        }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
        xhr.open(methon="POST",url='/scpg_submit/',async=true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange=function () {
                if(xhr.readyState == 4&& xhr.status == 200){
                scpg_obj= JSON.parse(xhr.responseText);
                if (scpg_obj.error_text == "正常"){
                    writeText(error_td,"");
                    writeText(phonemuber_td,scpg_obj.phonemuber);
                    writeText(city_td,scpg_obj.user_city);
                    writeText(district_td,scpg_obj.district);
                    writeText(county_td,scpg_obj.county);
                    writeText(citizen_or_villager_td,scpg_obj.citizen_or_villager);
                    writeText(star_td,scpg_obj.star);
                    writeText(begin_td,scpg_obj.begin);
                    writeText(length_of_time_td,scpg_obj.length_of_time);
                    writeText(phone_brand_td,scpg_obj.phone_brand);
                    writeText(is_header_user_td,scpg_obj.is_header_user);
                    writeText(is_risk_user_td,scpg_obj.is_risk_user);
                    writeText(phone_type_td,scpg_obj.phone_type);
                    app_option.series.data = scpg_obj.app[0];
                    app.clear();
                    app.setOption(app_option);
                    Apru_option.series.data= scpg_obj.arpu;
                    apru.clear();
                    apru.setOption(Apru_option);
                    dou_option.series.data = scpg_obj.dou;
                    dou.clear();
                    dou.setOption(dou_option);
                    call_time.innerHTML="";
                    call_time.innerHTML=(scpg_obj.call_time).toString();
                    writeText(date_td,time);
                    writeText(yhdh_td,phone_number);
                    writeText(ztcmc_td,scpg_obj.ztcmc);
                    writeText(lldy500M_td,scpg_obj.lldy500M);
                    writeText(xykh_td,scpg_obj.xykh);
                    writeText(ctcyh_td,scpg_obj.ctcyh);
                    writeText(yjarpu_td,scpg_obj.yjarpu);
                    writeText(qarpuyh_td,scpg_obj.qarpuyh);
                    writeText(yjdou_td,scpg_obj.yjdou);
                    writeText(doupm_td,scpg_obj.doupm);
                    writeText(zdpp_td,scpg_obj.zdpp);
                    writeText(zdxh_td,scpg_obj.zdxh);
                    writeText(lwyj_td,scpg_obj.lwyj);
                    writeText(tsyh_td,scpg_obj.tsyh);
                    writeText(bmyyh_td,scpg_obj.bmyyh);
                }
                else{
                    writeText(error_td,scpg_obj.error_text);
                }
            }else{
                }

    }
    xhr.send('phone_number='+phone_number);
}
//onload事件
function scpg_onload(){
     var now_time=new Date;
     var time=now_time.getFullYear().toString()+"年"+(now_time.getMonth()+1).toString()+"月"+now_time.getDate().toString()+"日";
        //+ now_time.getHours()+"时"+now_time.getMinutes()+"分";
    var xhr;
    if(window.XMLHttpRequest){
        xhr= new XMLHttpRequest();
    }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
    xhr.open(methon="POST",url='/scpg_onload/',async=true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange=function () {
        if(xhr.readyState == 4&& xhr.status == 200){
            scpg_obj= JSON.parse(xhr.responseText);
            if (scpg_obj.error_text == "正常" && scpg_obj.phonemuber != ""){
                writeText(error_td,"");
                writeText(phonemuber_td,scpg_obj.phonemuber);
                writeText(city_td,scpg_obj.user_city);
                writeText(district_td,scpg_obj.district);
                writeText(county_td,scpg_obj.county);
                writeText(citizen_or_villager_td,scpg_obj.citizen_or_villager);
                writeText(star_td,scpg_obj.star);
                writeText(begin_td,scpg_obj.begin);
                writeText(length_of_time_td,scpg_obj.length_of_time);
                writeText(phone_brand_td,scpg_obj.phone_brand);
                writeText(is_header_user_td,scpg_obj.is_header_user);
                writeText(is_risk_user_td,scpg_obj.is_risk_user);
                writeText(phone_type_td,scpg_obj.phone_type);
                app_option.series.data = scpg_obj.app[0];
                app.clear();
                app.setOption(app_option);
                Apru_option.series.data= scpg_obj.arpu;
                apru.clear();
                apru.setOption(Apru_option);
                dou_option.series.data = scpg_obj.dou;
                dou.clear();
                dou.setOption(dou_option);
                call_time.innerHTML="";
                call_time.innerHTML=(scpg_obj.call_time).toString();
                writeText(date_td,time);
                writeText(yhdh_td,phone_number);
                writeText(ztcmc_td,scpg_obj.ztcmc);
                writeText(lldy500M_td,scpg_obj.lldy500M);
                writeText(xykh_td,scpg_obj.xykh);
                writeText(ctcyh_td,scpg_obj.ctcyh);
                writeText(yjarpu_td,scpg_obj.yjarpu);
                writeText(qarpuyh_td,scpg_obj.qarpuyh);
                writeText(yjdou_td,scpg_obj.yjdou);
                writeText(doupm_td,scpg_obj.doupm);
                writeText(zdpp_td,scpg_obj.zdpp);
                writeText(zdxh_td,scpg_obj.zdxh);
                writeText(lwyj_td,scpg_obj.lwyj);
                writeText(tsyh_td,scpg_obj.tsyh);
                writeText(bmyyh_td,scpg_obj.bmyyh);
                }
    }
    }
    xhr.send();
}