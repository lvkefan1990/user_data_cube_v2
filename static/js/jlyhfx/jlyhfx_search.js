function chaxun(){
    var city_index=city_select.selectedIndex;//城市选择
    var city = city_select.options[city_index].text;//获得城市
    var district_index = district_select.selectedIndex;
    var district = district_select[district_index].text;//获得区县
    var formwork_index = formwork_select.selectedIndex;
    var formwork = formwork_select[formwork_index].text;//获取模板类型
    if(city=="--请选择--" || district =="--请选择--" || district ==""){
        alert("地市和区县不能为空")
    }
    else{
        var xhr;
        if(window.XMLHttpRequest){
            xhr= new XMLHttpRequest();
        }else{xhr = new ActiveXObject("Microsoft.XMLHTTP")};
        xhr.open(methon="POST",url='/jlyhfx_submit/',async=true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhr.onreadystatechange=function ()
        {
            if(xhr.readyState == 4&& xhr.status == 200)
            {
                jlyhfx_obj= JSON.parse(xhr.responseText);
                trs_head = export_table_thead.getElementsByTagName("tr");
                export_table_thead.removeChild(trs_head[0]);//表头只有一个tr
                tr_head = document.createElement('tr');
                for(table_head_col in jlyhfx_obj.table_head){
                    td=document.createElement('td');
                    writeText(td,jlyhfx_obj.table_head[table_head_col]);
                    tr_head.appendChild(td);
                }
                export_table_thead.appendChild(tr_head);
                //至此写完了表头,写下来写body
                trs_body = export_table_tbody.getElementsByTagName("tr");
                for(i=trs_body.length-1;i>=0;i--){
                    export_table_tbody.removeChild(trs_body[i]);
                    };
                for(table_row in jlyhfx_obj.table_body){
                    tr_s = document.createElement('tr');
                    for(table_td in jlyhfx_obj.table_body[table_row]){
                        td=document.createElement('td');
                        writeText(td,jlyhfx_obj.table_body[table_row][table_td]);
                        tr_s.appendChild(td);
                    }
                    export_table_tbody.appendChild(tr_s);
                }
            }
        }
         xhr.send("city="+city +"&district="+district+"&formwork="+formwork);
    }
}