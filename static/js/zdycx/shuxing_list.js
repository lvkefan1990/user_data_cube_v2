//定义显示和隐藏的函数
function xianshi_yincang(checkbox,div_list_block,div_list_none) {
    if(checkbox.checked==true) {
        var i = 0;
        while (i < div_list_block.length) {
            my_div= document.getElementById(div_list_block[i]);
            my_div.style.display = "block";
            i = i+1;
        }
    } else if(checkbox.checked ==false){
        var j = 0;
        while(j<div_list_none.length){
            my_div= document.getElementById(div_list_none[j]);
            my_div.style.display = "none";
            j = j+1;
        }
    }
}

//全选事件
function quanxuan(checkbox,name="",inputlist=[]){
        var items = document.getElementsByName(name);
        if(checkbox.checked == true){
            for (i = 0; i < items.length; i++) {
                items[i].checked = true;
            }
            for(j = 0; j < inputlist.length; j++){
                var input_ele = document.getElementById(inputlist[j]);
                input_ele.disabled = false;
            }
        }
        else if(checkbox.checked == false){
            for (i = 0; i < items.length; i++) {
                items[i].checked = false;
            }
            for(j = 0; j < inputlist.length; j++){
                var input_ele = document.getElementById(inputlist[j]);
                input_ele.value = "";
                input_ele.disabled = true;
            }
        }
}

//全选中的单选框事件
function quanxuan_radio(checkbox,name="",radiolist=[]){
        var items = document.getElementsByName(name);
        if(checkbox.checked == true){
            for (i = 0; i < items.length; i++) {
                items[i].checked = true;
            }
            for(j = 0; j < inputlist.length; j++){
                var input_ele = document.getElementById(inputlist[j]);
                input_ele.disabled = false;
            }
        }
        else if(checkbox.checked == false){
            for (i = 0; i < items.length; i++) {
                items[i].checked = false;
            }
            for(j = 0; j < inputlist.length; j++){
                var input_ele = document.getElementById(inputlist[j]);
                input_ele.value = "";
                input_ele.disabled = true;
            }
        }
}

//条件设置
function tiaojian_shezhi(checkbox,id_list=[]){
        if(checkbox.checked == true){
            for (i = 0; i < id_list.length; i++) {
                var id_ele = document.getElementById(id_list[i]);
                id_ele.disabled = false;
            }
        }
        else if(checkbox.checked == false){
            for (i = 0; i < id_list.length; i++) {
                var id_ele = document.getElementById(id_list[i]);
                id_ele.innerHTML = "";
                id_ele.disabled = true;
            }
        }
}

//单选设置
function tiaojian_radio(checkbox,name="",id_list=[]){
    var radio_list = document.getElementsByName(name);
        if(checkbox.checked == true){
            for (i = 0; i < radio_list.length; i++) {
                radio_list[i].disabled = false;
            }
        }
        else if(checkbox.checked == false){
            radio_list[0].checked = true;
             for (i = 0; i < radio_list.length; i++) {
                radio_list[i].disabled = true;
            }
        }
}
//单选项目的全选
function quanxuan_radio(checkbox,name="",name_list=[],id_list=[]){
    var items = document.getElementsByName(name);
    if(checkbox.checked == true){
        for (k = 0; k < items.length; k++) {
                items[k].checked = true;
            }
        for (i = 0; i < name_list.length; i++){
            var radio_list = document.getElementsByName(name_list[i]);
            for (j = 0; j < radio_list.length; j++){
                radio_list[j].disabled = false;
            }
        }
    }
    else if(checkbox.checked == false){
        for (k = 0; k < items.length; k++) {
                items[k].checked = false;
            }
        for (i = 0; i < name_list.length; i++){
            var radio_list = document.getElementsByName(name_list[i]);
            radio_list[0].checked = true;
            for (j = 0; j < radio_list.length; j++){
                radio_list[j].disabled = true;
            }
        }
    }
}
//条件的确认
function tiaojian_queren(name_list=[]){
    zdycx_json = {
        condition:{
        "地市":"",
        "区县":[],
        "起始时间":"",
        "终止时间":"",
        },
        result:['地市','区县','起始时间','终止时间','电话号码'],
        change:0,}
        //初始化json
    console.log(zdycx_json);
    condition_ul.innerHTML = "";
    column_ul.innerHTML= "";
    //获得市级名称
    var city_index=city_select.selectedIndex;//城市选择
    var city = city_select.options[city_index].text;//获得城市
    city_condition_li=document.createElement('li');
    writeText(city_condition_li,"地市： "+city);
    condition_ul.appendChild(city_condition_li);
    zdycx_json.condition["地市"] = city;
    //获得区县名称
    var districts = document.getElementsByName("district");//获得城市
    districts_condition_li = document.createElement('li');
    textNode_districts = document.createTextNode("区县：");
    districts_condition_li.appendChild(textNode_districts);
    districts_list = [];
    for(i=1;i<districts.length;i++){
        if(districts[i].checked ==true){
            textNode=document.createTextNode(districts[i].value+" ");
            districts_condition_li.appendChild(textNode);
            districts_list.push(districts[i].value);
        }
    }
    condition_ul.appendChild(districts_condition_li);
    zdycx_json.condition["区县"] = districts_list;
    //获得起始和终止时间
    strat_time_condition_li = document.createElement('li');
    writeText(strat_time_condition_li,"起始时间："+$("#start_datetimepicker").val());
    condition_ul.appendChild(strat_time_condition_li);
    zdycx_json.condition["起始时间"] = $("#start_datetimepicker").val();
    end_time_condition_li = document.createElement('li');
    writeText(end_time_condition_li,"终止时间："+$("#end_datetimepicker").val());
    condition_ul.appendChild(end_time_condition_li);
    zdycx_json.condition["终止时间"] = $("#end_datetimepicker").val();
    //接下来写用户自定义的部分
    for(i=0;i<name_list.length;i++){
        var condition_items = document.getElementsByName(name_list[i]);
        console.log(linshi_condition_items);
         for(j=1;j<condition_items.length;j++){
             if(condition_items[j].checked ==true){
                if(condition_list.indexOf(condition_items[j].value)>=0){
                    var linshi_condition_items=document.getElementsByName(condition_items[j].value);
                    console.log(linshi_condition_items);
                    if(linshi_condition_items[0].type=="text"){
                        if(parseFloat(linshi_condition_items[0].value)<=parseFloat(linshi_condition_items[1].value)){
                            var linshi_list =[];
                            linshi_list.push(linshi_condition_items[0].value);
                            linshi_list.push(linshi_condition_items[1].value);
                            condition_li = document.createElement('li');
                            writeText(condition_li,condition_items[j].value+"范围："+linshi_list[0].toString()+"-"+linshi_list[1].toString());
                             condition_ul.appendChild(condition_li);
                             zdycx_json.condition[condition_items[j].value] = linshi_list;
                        }
                        else{
                            alert("起始值必须小于终止值")
                        }
                    }
                    else if(linshi_condition_items[0].type=="radio"){
                        for(k=0;k<linshi_condition_items.length;k++) {
                            if (linshi_condition_items[k].checked == true) {
                                condition_li = document.createElement('li');
                                writeText(condition_li, condition_items[j].value + "：" + linshi_condition_items[k].value);
                                condition_ul.appendChild(condition_li);
                                 zdycx_json.condition[condition_items[j].value] = linshi_condition_items[k].value;
                            }
                        }
                    }
                }
             }
         }
    }

    //接下来写查询的结果字段
    for(i=0;i<name_list.length;i++){
        var items = document.getElementsByName(name_list[i]);
        //j从1开始，因为items[0]是全选
        for(j=1;j<items.length;j++){
            if(items[j].checked ==true){
                 column_li=document.createElement('li');
                 writeText(column_li,items[j].value);
                 column_ul.appendChild(column_li);
                 zdycx_json.result.push(items[j].value);
            }
        }
    }
    zdycx_json.change = 1;
    console.log(zdycx_json);
}
