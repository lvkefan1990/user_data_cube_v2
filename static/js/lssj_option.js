var lssj__cover_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['优','差']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: [],
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'优',
            type:'line',
            data:[],
        },
        {
            name:'差',
            type:'line',
            data:[],
        }
    ]
};
var lssj_call_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['通话成功率']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'通话成功率',
            type:'line',
            data:[]
        },
    ]
};
var lssj_speed_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['全业务上行速率','全业务下行速率']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'全业务上行速率',
            type:'line',
            data:[]
        },
        {
            name:'全业务下行速率',
            type:'line',
            data:[]
        }
    ]
};
var lssj_ete_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['优','差']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ["round1,round2,round3"]
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'优',
            type:'line',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'差',
            type:'line',
            data:[220, 182, 191, 234, 290, 330, 310]
        }
    ]
};
var lssj_core_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['优','差']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ["round1,round2,round3"]
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'优',
            type:'line',
            data:[120, 132, 101, 134, 90, 230, 210]
        },
        {
            name:'差',
            type:'line',
            data:[220, 182, 191, 234, 290, 330, 310]
        }
    ]
};
var lssj_expense_option = {
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['用户月均流量','用户月均消费量']
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name:'用户月均流量',
            type:'line',
            data:[],
        },
        {
            name:'用户月均消费量',
            type:'line',
            data:[],
        }
    ]
};
