const options = {
	series         : [{
		name : "table",
		data : [
			["2022-01-01", 6593.34, 6600, 6582.63, 6600],
			["2022-01-02", 6595.16, 6604.76, 6590.73, 6593.86]
		]
	}],
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
				upward: "#FF6B6B",
				downward: "#4D96FF"
			}
		}
	}
};

const chart = new ApexCharts(document.querySelector("#chart-area"), options);
chart.render();
