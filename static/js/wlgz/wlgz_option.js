//第一个是覆盖图，使用的是饼图，环形图
var coverage_option ={
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
                {name:'优',value:0},
                {name:'良',value:0},
                {name:'差',value:0},
            ]
        },
};
//第二个是rsrp图，使用仪表图
var rsrp_option = {
    tooltip : {
        formatter: "{c}dbm"
    },
    series:
        {
            type: 'gauge',
            min:-140,
            max:-50,
            splitNumber:3,
            radius: '88%',
            axisLine: {            // 坐标轴线
                lineStyle: {       // 属性lineStyle控制线条样式
                    color: [[0.33, '#e69d87'],[0.48, '#759aa0'],[1, '#dd6b66']],
                    width: 12,
                }
            },
            pointer:{
                 width:6,
            },
            splitLine: {           // 分隔线
                length :18,         // 属性length控制线长
            },
            axisTick: {            // 坐标轴小标记
                length :12,        // 属性length控制线长
            },
            detail: {
                formatter:'{value}dbm',
                fontSize:20,
            },
            data: [{value: -67, name: ''}],
        }
};

//第三个下载速率图，使用水球图
var dl_speed_option = {
    tooltip : {
        formatter: "{c}k/S"
    },
    series:
        {
            type: 'gauge',
            min:0,
            max:30000,
            splitNumber:3,
            radius: '88%',
            axisLine: {            // 坐标轴线
                lineStyle: {       // 属性lineStyle控制线条样式
                    color: [[0.33, '#e69d87'],[0.66, '#759aa0'],[1, '#dd6b66']],
                    width: 12,
                }
            },
            pointer:{
                 width:6,
            },
            splitLine: {           // 分隔线
                length :18,         // 属性length控制线长
            },
            axisTick: {            // 坐标轴小标记
                length :12,        // 属性length控制线长
            },
            detail: {
                formatter:'{value}k/s',
                fontSize:20,
            },
            data: [{value: 6677, name: ''}],
        }
};
//第四个通话成功率图，使用仪表盘
var call_success_option = {
    tooltip : {
        formatter: "{c}%"
    },
    series:
        {
            type: 'gauge',
            min:0,
            max:100,
            splitNumber:4,
            radius: '88%',
            axisLine: {            // 坐标轴线
                lineStyle: {       // 属性lineStyle控制线条样式
                    color: [[0.9, '#e69d87'],[0.95, '#759aa0'],[1, '#dd6b66']],
                    width: 12,
                }
            },
            pointer:{
                 width:6,
            },
            splitLine: {           // 分隔线
                length :18,         // 属性length控制线长
            },
            axisTick: {            // 坐标轴小标记
                length :12,        // 属性length控制线长
            },
            detail: {
                formatter:'{value}%',
                fontSize:20,
            },
            data: [{value: 100, name: ''}],
        }
};