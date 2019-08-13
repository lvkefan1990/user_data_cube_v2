portrait_option = {
    tooltip: {},
    legend: {
        data: ['R_1'],
        top:'0px',
    },
    radar: {
        center:['50%','55%'],
        // shape: 'circle',
        name: {
            textStyle: {
                color: '#fff',
                backgroundColor: '#000',
                padding: [3, 5]
           }
        },
        indicator: [
           { name: '价值评估', max:100},
           { name: '覆盖评估', max: 100},
           { name: '速率评估', max: 100},
           { name: '端到端评估', max: 100},
           { name: '敏感性评估', max: 100},
        ]
    },
    series: {
        type: 'radar',
        // areaStyle: {normal: {}},
        data : [
            {
                value : [],
                name : 'R_1'
            }
        ]
    }
};