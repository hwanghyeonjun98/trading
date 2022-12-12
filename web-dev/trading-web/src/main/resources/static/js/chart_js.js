const options = {
	series         : [],
	chart          : {
		type          : "candlestick",
		height        : 350,
		locales       : [{
			"name"    : "ko",
			"options" : {
				"months"      : ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
				"shortMonths" : ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
				"days"        : ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"],
				"shortDays"   : ["일", "월", "화", "수", "목", "금", "토"],
				"toolbar"     : {
					"menu"          : "메뉴",
					"selection"     : "영역선택",
					"selectionZoom" : "선택 후 확제",
					"zoomIn"        : "확대",
					"zoomOut"       : "축소",
					"pan"           : "이동",
					"reset"         : "초기화"
				}
			}
		}],
		defaultLocale : "ko",
		toolbar       : {
			tools : {
				download : false,
				reset: '<i class="bi bi-arrow-counterclockwise" style="font-size:20px;"></i>'
			}
		}
	}, tooltip     : {
		enabled : true,
		x       : {
			show   : true,
			format : "MM/dd",
		}
	}, xaxis       : {
		type   : "datetime",
		labels : {
			datetimeFormatter : {
				year  : "yyyy년",
				month : "MM월 dd일",
				day   : "MM월 dd일"
			}
		}
	}, yaxis       : {
		tooltip : {
			enabled : true,
		}
	}, plotOptions : {
		candlestick : {
			colors : {
				upward   : "#FF6B6B",
				downward : "#4D96FF"
			}
		}
	}, noData      : {
		text          : "데이터가 없습니다.",
		align         : "center",
		verticalAlign : "middle",
		style         : {
			fontSize : "2.4rem"
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



