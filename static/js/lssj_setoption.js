function chaxun() {
        var now_time=new Date;
        var time=now_time.getFullYear().toString()+"年"+(now_time.getMonth()+1).toString()+"月"+now_time.getDate().toString()+"日";
        //+ now_time.getHours()+"时"+now_time.getMinutes()+"分";
        var phone_number = document.getElementById("phone_number").value;
        var xhr;
        if(window.XMLHttpRequest){
            xhr= new XMLHttpRequest();
        }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
        xhr.open(methon="POST",url='/lssj_submit/',async=true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange=function () {
                if(xhr.readyState == 4&& xhr.status == 200){
                lssj_obj= JSON.parse(xhr.responseText);
                if (lssj_obj.error_text == "正常"){
                    writeText(error_td,"");
                    writeText(phonemuber_td,lssj_obj.phonemuber);
                    writeText(city_td,lssj_obj.user_city);
                    writeText(district_td,lssj_obj.district);
                    writeText(county_td,lssj_obj.county);
                    writeText(citizen_or_villager_td,lssj_obj.citizen_or_villager);
                    writeText(star_td,lssj_obj.star);
                    writeText(begin_td,lssj_obj.begin);
                    writeText(length_of_time_td,lssj_obj.length_of_time);
                    writeText(phone_brand_td,lssj_obj.phone_brand);
                    writeText(is_header_user_td,lssj_obj.is_header_user);
                    writeText(is_risk_user_td,lssj_obj.is_risk_user);
                    writeText(phone_type_td,lssj_obj.phone_type);
                    lssj__cover_option.xAxis.data = lssj_obj.xaxis;
                    lssj__cover_option.series[0].data=lssj_obj.good_cover;
                    lssj__cover_option.series[1].data=lssj_obj.bad_cover;
                    lssj_call_option.xAxis.data = lssj_obj.xaxis;
                    lssj_call_option.series[0].data=lssj_obj.call_success;
                    lssj_speed_option.xAxis.data = lssj_obj.xaxis;
                    lssj_speed_option.series[0].data=lssj_obj.ul_speed;
                    lssj_speed_option.series[1].data=lssj_obj.dl_speed;
                    lssj_expense_option.xAxis.data=lssj_obj.xaxis;
                    lssj_expense_option.series[0].data=lssj_obj.dou;
                    lssj_expense_option.series[1].data=lssj_obj.arpu;
                    fggz();
                    trs = lssj_table_tbody.getElementsByTagName("tr");
                    for(i=trs.length-1;i>=0;i--){
                    lssj_table_tbody.removeChild(trs[i]);
                    }
                     for(table_obj in lssj_obj.export_table){
                         if (table_obj.search(/row/i) != -1){
                             tr=document.createElement('tr');
                             for(i=0;i<lssj_obj.export_table.attr_count;i++){
                                    td=document.createElement('td');
                                    writeText(td,lssj_obj.export_table[table_obj][i]);
                                    tr.appendChild(td);
                             }
                         }
                         lssj_table_tbody.appendChild(tr);
                     }
                }
                else{
                    writeText(error_td,wlgz_obj.error_text);
                }
            }else{
            }
    }
    xhr.send('phone_number='+phone_number);
}
function fggz(){
    $("#fggz_li").removeClass("content_l_t_tabs_select");
    $("#thgz_li").removeClass("content_l_t_tabs_select");
    $("#slgz_li").removeClass("content_l_t_tabs_select");
    $("#zfnl_li").removeClass("content_l_t_tabs_select");
    $("#fggz_li").addClass("content_l_t_tabs_select");
    lssj_echarts.clear();
    lssj_echarts.setOption(lssj__cover_option);
}
function thgz(){
    $("#fggz_li").removeClass("content_l_t_tabs_select");
    $("#thgz_li").removeClass("content_l_t_tabs_select");
    $("#slgz_li").removeClass("content_l_t_tabs_select");
    $("#zfnl_li").removeClass("content_l_t_tabs_select");
    $("#thgz_li").addClass("content_l_t_tabs_select");
    lssj_echarts.clear();
    lssj_echarts.setOption(lssj_call_option);
}
function slgz(){
     $("#fggz_li").removeClass("content_l_t_tabs_select");
    $("#thgz_li").removeClass("content_l_t_tabs_select");
    $("#slgz_li").removeClass("content_l_t_tabs_select");
    $("#zfnl_li").removeClass("content_l_t_tabs_select");
    $("#slgz_li").addClass("content_l_t_tabs_select");
    lssj_echarts.clear();
    lssj_echarts.setOption(lssj_speed_option);
}
function zfnl(){
    $("#fggz_li").removeClass("content_l_t_tabs_select");
    $("#thgz_li").removeClass("content_l_t_tabs_select");
    $("#slgz_li").removeClass("content_l_t_tabs_select");
    $("#zfnl_li").removeClass("content_l_t_tabs_select");
    $("#zfnl_li").addClass("content_l_t_tabs_select");
    lssj_echarts.clear();
    lssj_echarts.setOption(lssj_expense_option);
}