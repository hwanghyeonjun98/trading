const options = {
	series         : [],
	chart          : {
		type : "candlestick", height : 350
	}, title       : {
		text : "내역", align : "left"
	}, xaxis       : {
		type : "datetime"
	}, yaxis       : {
		tooltip : {
			enabled : true
		}
	}, plotOptions : {
		candlestick : {
			colors : {
				upward   : "#FF6B6B",
				downward : "#4D96FF"
			}
		}
	}
};

const chart = new ApexCharts(document.querySelector("#chart-area"), options);
chart.render();

// 기본 호출
const defaulturl = "/api/data/chart/aedkrw내역";
$.getJSON(defaulturl, function (response) {
	let dataList = [];

	response.forEach((item) => {
		dataList.push([item.dates, item.opens, item.highs, item.lows, item.closes]);
	});

	chart.updateSeries([{
		name : "table",
		data : dataList
	}]);
});
