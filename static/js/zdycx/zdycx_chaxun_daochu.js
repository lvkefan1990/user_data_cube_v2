function zdycx_chaxun(){
    console.log(zdycx_json);
    if(zdycx_json.change == 0){
        alert("您所输入的条件未符合要求");
    }
    else{
        var table_width=0;
        $.ajax({
            async:true,
            //data:zdycx_json,
            data:JSON.stringify(zdycx_json),
            dataType:"json",
            url:'/zdycx_submit/',
            type:"POST",
            success:function (data) {
                console.log(data);
                if(data.error !="正常"){
                    alert(data.error);
                }
                else{
                $("#export").attr("disabled",false).css("pointer-events","auto");
                trs_head = export_table_thead.getElementsByTagName("tr");
                export_table_thead.removeChild(trs_head[0]);//表头只有一个tr
                tr_head = document.createElement('tr');
                for(table_head_col in data.table_head){
                    td=document.createElement('td');
                    td.style.whiteSpace="nowrap";
                    td.style.width = "120px";
                    table_width = table_width+120;
                    writeText(td,data.table_head[table_head_col]);
                    tr_head.appendChild(td);
                }
                export_table_thead.appendChild(tr_head);
                export_table.style.width = (table_width*1.2).toString()+"px";
                export_table.style.tableLayout = "fixed";
                //完成表头的书写;
                export_table.style.width = (table_width*1.2).toString()+"px";
                numCount=data.table_body.length;
                pageNum = parseInt(numCount/pageCount);
                if(0 != numCount%pageCount){
                pageNum += 1;//获得总页数
                };
                //表体结构
                trs_body = export_table_tbody.getElementsByTagName("tr");
                for(i=trs_body.length-1;i>=0;i--){
                    export_table_tbody.removeChild(trs_body[i]);
                    };
                for(table_row in data.table_body){
                    tr_s = document.createElement('tr');
                    for(table_td in data.table_body[table_row]){
                        td=document.createElement('td');
                        td.style.width = "120px";
                        td.style.whiteSpace="nowrap";
                        td.style.overflow = "hidden";
                        td.style.textOverflow = "ellipsis";
                        writeText(td,data.table_body[table_row][table_td]);
                        tr_s.appendChild(td);
                }
                    export_table_tbody.appendChild(tr_s);
                }
                firstPage();
            }},
            error:function () {
                alert("Ajax错误");
            },
            beforeSend:function () {
                $("#zdycx_search").attr("disabled",true).css("pointer-events","none");
            },
            complete: function () {
                $("#zdycx_search").attr("disabled",false).css("pointer-events","auto");
            },
        })
    }
}