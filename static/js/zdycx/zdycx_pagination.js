//定义table
var numCount = 0;       //数据总数量
var columnsCounts = 0;  //数据列数量
var pageCount = 10;      //每页显示的数量
var pageNum = 1;        //总页数
var currPageNum = 1;   //当前页数

//页面标签变量
var blockTable=document.getElementById("export_table");//table对象;
var preSpan = document.getElementById("spanPre");//上一页;
var firstSpan =document.getElementById("spanFirst") ;//第一页
var nextSpan = document.getElementById("spanNext");//下一页
var lastSpan = document.getElementById("spanLast");//最后一页
var pageNumSpan =document.getElementById("spanTotalPage");//总页数
var currPageSpan =document.getElementById("spanPageNum");//当前页数

//显示第一页
function firstPage(){
    hide();//隐藏所有元素
    currPageNum = 1;
    showCurrPage(currPageNum);//设置span为当前页
    showTotalPage();//显示总页数
    for(i = 1; i < pageCount + 1; i++){
        blockTable.rows[i].style.display = "";
    }//显示这十项数据
    firstText();//span显示First
    preText();//span显示pre
    nextLink();//下一页可以用
    lastLink();//最后一页可以用
}
function prePage(){
    //前一页肯定每到最后一页
    hide();
    currPageNum--;//当前页数减一
    showCurrPage(currPageNum);
    showTotalPage();
    var firstR = firstRow(currPageNum);
    var lastR = lastRow(firstR);
    for(i = firstR; i < lastR; i++){
        blockTable.rows[i].style.display = "";
    }
    if(1 == currPageNum){
        firstText();
        preText();
        nextLink();
        lastLink();
    }else if(pageNum == currPageNum){
        preLink();
        firstLink();
        nextText();
        lastText();
    }else{
        firstLink();
        preLink();
        nextLink();
        lastLink();
    }
}

function nextPage(){
    hide();
    currPageNum++;
    showCurrPage(currPageNum);
    showTotalPage();
    var firstR = firstRow(currPageNum);
    var lastR = lastRow(firstR);
    for(i = firstR; i < lastR; i ++){
        blockTable.rows[i].style.display = "";
    }

    if(1 == currPageNum){
        firstText();
        preText();
        nextLink();
        lastLink();
    }else if(pageNum == currPageNum){
        preLink();
        firstLink();
        nextText();
        lastText();
    }else{
        firstLink();
        preLink();
        nextLink();
        lastLink();
    }
}
function lastPage(){
    hide();
    currPageNum = pageNum;
    showCurrPage(currPageNum);
    showTotalPage();
    var firstR = firstRow(currPageNum);
    for(i = firstR; i < numCount + 1; i++){
        blockTable.rows[i].style.display = "";
    }
    firstLink();
    preLink();
    nextText();
    lastText();
}
// 计算将要显示的页面的首行和尾行
function firstRow(currPageNum){
    return pageCount*(currPageNum - 1) + 1;
}

function lastRow(firstRow){
    var lastRow = firstRow + pageCount;
    if(lastRow > numCount + 1){
        lastRow = numCount + 1;
    }
    return lastRow;
}
//隐藏所有行
function hide(){
    for(var i = 1; i < numCount + 1; i ++){
        blockTable.rows[i].style.display = "none";
    }
}
//显示当前页数
function showCurrPage(cpn){
    currPageSpan.innerHTML = cpn;
}
//显示总页数
function showTotalPage(){
    pageNumSpan.innerHTML = pageNum;
}

//控制首页等功能的显示与不显示
function firstLink(){firstSpan.innerHTML = "<a href='javascript:firstPage();' style='color:#ffffff'>第一页</a>";}
function firstText(){firstSpan.innerHTML = "第一页";}

function preLink(){preSpan.innerHTML = "<a href='javascript:prePage();' style='color:#ffffff'>上一页</a>";}
function preText(){preSpan.innerHTML = "上一页";}

function nextLink(){nextSpan.innerHTML = "<a href='javascript:nextPage();' style='color:#ffffff'>下一页</a>";}
function nextText(){nextSpan.innerHTML = "下一页";}

function lastLink(){lastSpan.innerHTML = "<a href='javascript:lastPage();' style='color:#ffffff'>最后一页</a>";}
function lastText(){lastSpan.innerHTML = "最后一页";}
