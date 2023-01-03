let chartUrl = "/api/data/index/chart/kospi";

$.getJSON(chartUrl, function (response) {
	let dataList = [];

	response.forEach((item) => {
		dataList.push([item.dates, item.closes]);
	});

	chart.updateSeries([{
		name : "KOSPI",
		data : dataList
	}]);
});

var troptions = {
    series: [
    {
        name: '코스피',
        data: dataList(new Date('11 Feb 2017 GMT').getTime(), 20, {
        min: 10,
        max: 60
        })
    },
    {
        name: '코스닥',
        data: dataList(new Date('11 Feb 2017 GMT').getTime(), 20, {
        min: 10,
        max: 20
        })
    },
    {
        name: '합계',
        data: dataList(new Date('11 Feb 2017 GMT').getTime(), 20, {
        min: 10,
        max: 15
        })
    }
    ],
    chart: {
    type: 'area',
    height: 350,
    stacked: true,
    events: {
        selection: function (chart, e) {
        console.log(new Date(e.xaxis.min))
        }
    },
    },
    colors: ['#008FFB', '#00E396', '#CED4DC'],
    dataLabels: {
    enabled: false
    },
    stroke: {
    curve: 'smooth'
    },
    fill: {
    type: 'gradient',
    gradient: {
        opacityFrom: 0.6,
        opacityTo: 0.8,
    }
    },
    legend: {
    position: 'top',
    horizontalAlign: 'left'
    },
    xaxis: {
    type: 'datetime'
    },
    };

    var chart = new ApexCharts(document.querySelector("#chart3"), troptions);
    chart.render();
