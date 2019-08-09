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
        formatter: "{b} : {c}dbm"
    },
    series:
        {
            type: 'gauge',
            detail: {formatter:'{value}dbm'},
            data: [{value: -67, name: 'rsrp'}],
        }
};

//第三个下载速率图，使用水球图
var dl_speed_option = {
    tooltip : {
        formatter: "{c}M/s"
    },
    series:
        {
            type: 'gauge',
            detail: {formatter:'{value}M/s'},
            data: [{value: 30, name: 'rsrp'}],
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
            detail: {formatter:'{value}%'},
            data: [{value: 99, name: 'rsrp'}],
        }
};
//第五个app图，使用饼图（实心）
var app_option={
                    tooltip: {
                        formatter: '{d}%'
                    },
                    title: {
                        textStyle:{
                            fontWeight:'normal',
                            fontFamily:'Microsoft YaHei',
                            fontSize:14,
                            color:'#000000',
                        },
                        text: '前五位app'
                    },
                    series :
                        [{
                            type : 'pie',
                            percentPrecision: 1,
                            data : [1235, 6332, 2433],
                            label: {
                                normal: {
                                    formatter: '{c} 占 {d}%'
                                }
                            }
                        }]
                };
//第六个dou图，使用仪表图
var dou_option={
                    tooltip: {
                        formatter: '{d}%'
                    },
                    title: {
                        textStyle:{
                            fontWeight:'normal',
                            fontFamily:'Microsoft YaHei',
                            fontSize:14,
                            color:'#000000',
                        },
                        text: '用户月均流量'
                    },
                    series :
                        [{
                            type : 'pie',
                            percentPrecision: 1,
                            data : [1235, 6332, 2433],
                            label: {
                                normal: {
                                    formatter: '{c} 占 {d}%'
                                }
                            }
                        }]
                };
//第七个apu图，使用仪表图
var apu_option ={
                    tooltip: {
                        formatter: '{d}%'
                    },
                    title: {
                        textStyle:{
                            fontWeight:'normal',
                            fontFamily:'Microsoft YaHei',
                            fontSize:14,
                            color:'#000000',
                        },
                        text: '用户月均消费量'
                    },
                    series :
                        [{
                            type : 'pie',
                            percentPrecision: 1,
                            data : [1235, 6332, 2433],
                            label: {
                                normal: {
                                    formatter: '{c} 占 {d}%'
                                }
                            }
                        }]
                };
//第八个通话时长图，使用仪表图
var call_time_option = {
                    tooltip: {
                        formatter: '{d}%'
                    },
                    title: {
                        textStyle:{
                            fontWeight:'normal',
                            fontFamily:'Microsoft YaHei',
                            fontSize:14,
                            color:'#000000',
                        },
                        text: '用户通话时长'
                    },
                    series :
                        [{
                            type : 'pie',
                            percentPrecision: 1,
                            data : [1235, 6332, 2433],
                            label: {
                                normal: {
                                    formatter: '{c} 占 {d}%'
                                }
                            }
                        }]
                };
//第九个用户画像图，使用雷达
var portrait_option= {
                    tooltip: {
                        formatter: '{d}%'
                    },
                    title: {
                        textStyle:{
                            fontWeight:'normal',
                            fontFamily:'Microsoft YaHei',
                            fontSize:14,
                            color:'#000000',
                        },
                        text: '用户画像图'
                    },
                    series :
                        [{
                            type : 'pie',
                            percentPrecision: 1,
                            data : [1235, 6332, 2433],
                            label: {
                                normal: {
                                    formatter: '{c} 占 {d}%'
                                }
                            }
                        }]
                };
