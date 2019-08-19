function writeText(element,content){
    if(typeof(element.innerText) === 'string'){
        element.innerText=content;
    }else{
        element.textContent=content;
    }
}

//定义下拉列表
var city_select = document.getElementById("city_select");
var district_select = document.getElementById("district_select");
var formwork_select = document.getElementById("formwork");

//定义输出表格及其父容器
var export_table = document.getElementById("export_table");
var export_table_thead = document.getElementById("export_table_thead");
var export_table_tbody = document.getElementById("export_table_tbody");

var content_l = document.getElementById("content_l");