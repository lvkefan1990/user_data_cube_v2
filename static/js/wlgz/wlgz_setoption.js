function chaxun() {
        var now_time=new Date;
        var time=now_time.getFullYear().toString()+"年"+(now_time.getMonth()+1).toString()+"月"+now_time.getDate().toString()+"日";
        //+ now_time.getHours()+"时"+now_time.getMinutes()+"分";
        var phone_number = document.getElementById("phone_number").value;
        var xhr;
        if(window.XMLHttpRequest){
            xhr= new XMLHttpRequest();
        }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
        xhr.open(methon="POST",url='/wlgz_submit/',async=true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange=function () {
            if(xhr.readyState == 4){
            $("#search").attr("disabled",false).css("pointer-events","auto");
                if(xhr.status == 200){
                  wlgz_obj= JSON.parse(xhr.responseText);
                if (wlgz_obj.error_text == "正常"){
                    writeText(error_td,"");
                    writeText(phonemuber_td,wlgz_obj.phonemuber);
                    writeText(city_td,wlgz_obj.user_city);
                    writeText(district_td,wlgz_obj.district);
                    writeText(county_td,wlgz_obj.county);
                    writeText(citizen_or_villager_td,wlgz_obj.citizen_or_villager);
                    writeText(star_td,wlgz_obj.star);
                    writeText(begin_td,wlgz_obj.begin);
                    writeText(length_of_time_td,wlgz_obj.length_of_time);
                    writeText(phone_brand_td,wlgz_obj.phone_brand);
                    writeText(is_header_user_td,wlgz_obj.is_header_user);
                    writeText(is_risk_user_td,wlgz_obj.is_risk_user);
                    writeText(phone_type_td,wlgz_obj.phone_type);
                    coverage_option.series.data = wlgz_obj.coverage;
                    cover.setOption(coverage_option);
                    rsrp_option.series.data[0].value = wlgz_obj.rsrp-140;
                    rsrp.setOption(rsrp_option);
                    dl_speed_option.series.data[0].value = wlgz_obj.dl_speed;
                    dl_speed.setOption(dl_speed_option);
                    call_success_option.series.data[0].value=wlgz_obj.call_success;
                    call_success.setOption(call_success_option);
                    writeText(date_td,time);
                    writeText(yhdh_td,phone_number);
                    writeText(yhczxq_td,wlgz_obj.resident_cell);
                    writeText(pjrsrp_td,(wlgz_obj.rsrp-140).toString()+"dbm");
                    writeText(fgl_td,(wlgz_obj.fgl*100).toString()+"%");
                    writeText(cphrl_td,wlgz_obj.cphrl+"%");
                    writeText(xhcgl_td,wlgz_obj.xhcgl+"%");
                    writeText(dxl_td,wlgz_obj.dxl+"%");
                    writeText(qywsxsl_td,wlgz_obj.qywsxsl);
                    writeText(qywxxsl_td,wlgz_obj.dl_speed);
                    //writeText(dbsxsl_td,wlgz_obj.dl_speed);
                    //writeText(dbxxsl_td,wlgz_obj.dl_speed);
                    writeText(http_td,wlgz_obj.httpcgl);
                    writeText(tcpcgl_td,wlgz_obj.tcpcgl);
                    writeText(tcpsy_td,wlgz_obj.tcpsy);
                    writeText(tcpwxcgl_td,wlgz_obj.tcpwxcgl);
                    writeText(tcpwxsy_td,wlgz_obj.tcpwxsy);
                    writeText(tcpwxsy_td,wlgz_obj.tcpwxsy);
                    writeText(tcpwxsy_td,wlgz_obj.tcpwxsy);
                    writeText(ymxysy_td,wlgz_obj.ymxysy);
                    writeText(qhcgl_td,wlgz_obj.qhcgl);
                    writeText(fwqqcgl_td,wlgz_obj.fwqqcgl);
                    writeText(fzcgl_td,wlgz_obj.fzcgl);
                    writeText(tau_td,wlgz_obj.tau);
                }
                else{
                    writeText(error_td,wlgz_obj.error_text);
                    writeText(phonemuber_td,"");
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
                    cover.clear();
                    rsrp.clear();
                    dl_speed.clear();
                    call_success.clear();
                    writeText(date_td,"");
                    writeText(yhdh_td,"");
                    writeText(yhczxq_td,"");
                    writeText(pjrsrp_td,"");
                    writeText(fgl_td,"");
                    writeText(cphrl_td,"");
                    writeText(xhcgl_td,"");
                    writeText(dxl_td,"");
                    writeText(qywsxsl_td,"");
                    writeText(qywxxsl_td,"");
                    //writeText(dbsxsl_td,wlgz_obj.dl_speed);
                    //writeText(dbxxsl_td,wlgz_obj.dl_speed);
                    writeText(http_td,"");
                    writeText(tcpcgl_td,"");
                    writeText(tcpsy_td,"");
                    writeText(tcpwxcgl_td,"");
                    writeText(tcpwxsy_td,"");
                    writeText(tcpwxsy_td,"");
                    writeText(tcpwxsy_td,"");
                    writeText(ymxysy_td,"");
                    writeText(qhcgl_td,"");
                    writeText(fwqqcgl_td,"");
                    writeText(fzcgl_td,"");
                    writeText(tau_td,"");
                }
                }
            }
        }
        xhr.send('phone_number='+phone_number);
        $("#search").attr("disabled",true).css("pointer-events","none");
}
//onload事件
function wlgz_onload(){
     var now_time=new Date;
     var time=now_time.getFullYear().toString()+"年"+(now_time.getMonth()+1).toString()+"月"+now_time.getDate().toString()+"日";
     var xhr;
     if(window.XMLHttpRequest){
         xhr= new XMLHttpRequest();
     }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
     xhr.open(methon="POST",url='/wlgz_onload/',async=true);
     xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
     xhr.onreadystatechange=function () {
         if(xhr.readyState == 4){
          $("#search").attr("disabled",false).css("pointer-events","auto");
         if( xhr.status == 200){
            wlgz_obj= JSON.parse(xhr.responseText);
         if (wlgz_obj.error_text == "正常" && wlgz_obj.phonemuber != ""){
                    writeText(error_td,"");
                    writeText(phonemuber_td,wlgz_obj.phonemuber);
                    writeText(city_td,wlgz_obj.user_city);
                    writeText(district_td,wlgz_obj.district);
                    writeText(county_td,wlgz_obj.county);
                    writeText(citizen_or_villager_td,wlgz_obj.citizen_or_villager);
                    writeText(star_td,wlgz_obj.star);
                    writeText(begin_td,wlgz_obj.begin);
                    writeText(length_of_time_td,wlgz_obj.length_of_time);
                    writeText(phone_brand_td,wlgz_obj.phone_brand);
                    writeText(is_header_user_td,wlgz_obj.is_header_user);
                    writeText(is_risk_user_td,wlgz_obj.is_risk_user);
                    writeText(phone_type_td,wlgz_obj.phone_type);
                    coverage_option.series.data = wlgz_obj.coverage;
                    cover.setOption(coverage_option);
                    rsrp_option.series.data[0].value = wlgz_obj.rsrp-140;
                    rsrp.setOption(rsrp_option);
                    dl_speed_option.series.data[0].value = wlgz_obj.dl_speed;
                    dl_speed.setOption(dl_speed_option);
                    call_success_option.series.data[0].value=wlgz_obj.call_success;
                    call_success.setOption(call_success_option);
                    writeText(date_td,time);
                    writeText(yhdh_td,wlgz_obj.phonemuber);
                    writeText(yhczxq_td,wlgz_obj.resident_cell);
                    writeText(pjrsrp_td,(wlgz_obj.rsrp-140).toString()+"dbm");
                    writeText(fgl_td,(wlgz_obj.fgl*100).toString()+"%");
                    writeText(cphrl_td,wlgz_obj.cphrl+"%");
                    writeText(xhcgl_td,wlgz_obj.xhcgl+"%");
                    writeText(dxl_td,wlgz_obj.dxl+"%");
                    writeText(qywsxsl_td,wlgz_obj.qywsxsl);
                    writeText(qywxxsl_td,wlgz_obj.dl_speed);
                    //writeText(dbsxsl_td,wlgz_obj.dl_speed);
                    //writeText(dbxxsl_td,wlgz_obj.dl_speed);
                    writeText(http_td,wlgz_obj.httpcgl);
                    writeText(tcpcgl_td,wlgz_obj.tcpcgl);
                    writeText(tcpsy_td,wlgz_obj.tcpsy);
                    writeText(tcpwxcgl_td,wlgz_obj.tcpwxcgl);
                    writeText(tcpwxsy_td,wlgz_obj.tcpwxsy);
                    writeText(tcpwxsy_td,wlgz_obj.tcpwxsy);
                    writeText(tcpwxsy_td,wlgz_obj.tcpwxsy);
                    writeText(ymxysy_td,wlgz_obj.ymxysy);
                    writeText(qhcgl_td,wlgz_obj.qhcgl);
                    writeText(fwqqcgl_td,wlgz_obj.fwqqcgl);
                    writeText(fzcgl_td,wlgz_obj.fzcgl);
                    writeText(tau_td,wlgz_obj.tau);

         }
     }
     }
     }
     xhr.send();
     //查询发生以后，禁用查询
     $("#search").attr("disabled",true).css("pointer-events","none");
}