//app图
var app_option ={
    tooltip : {
        trigger: 'item',
        formatter: "{b}:{d}%"
    },
    legend: {
        orient: 'vertical',
        left: 'left',

    },
    series :
        {
            type: 'pie',
            radius : ['50%','68%'],
            center: ['50%', '50%'],
            data:[
                {name:'111',value:111},
                {name:'111',value:111},
                {name:'111',value:111},
                {name:'111',value:111},
            ]
        },
    label:{
        display:false,
    }
};
//arpu图形
var Apru_option = {
    series: {
        type: 'liquidFill',
        radius:"80%",
        data:[],
        label: {
            normal: {
                formatter: function(param) {
                    return  param.value*500+"元"},
                textStyle: {
                    fontSize: 14,
                }
            }
        }
    }
};
//dou图形
var dou_option = {
    series: {
        type: 'liquidFill',
        radius:"80%",
        data:[],
        label: {
            normal: {
                formatter: function(param) {
                    return  param.value*30000+"K"},
                textStyle: {
                    fontSize: 14,
                }
            }
        }
    }
};