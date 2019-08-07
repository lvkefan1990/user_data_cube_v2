function chaxun() {
        var now_time=new Date;
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
                }
                else{
                    writeText(error_td,wlgz_obj.error_text);
                }
                this.disabled=false;
            }else{
                    this.disabled = true;
                }

    }
    xhr.send('phone_number='+phone_number);
    }