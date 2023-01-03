const options = {
	series        : [],
	chart         : {
		zoom          : {
			enabled : false
		},
		type          : "area",
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
			show : false

		}
	}, tooltip    : {
		enabled : true,
		x       : {
			show   : true,
			format : "MM/dd",
		}
	}, xaxis      : {
		type   : "datetime",
		labels : {
			datetimeFormatter : {
				year  : "yyyy년",
				month : "MM월 dd일",
				day   : "MM월 dd일"
			}
		}
	}, yaxis      : {
		tooltip : {
			enabled : true,
		}
	}, noData     : {
		text          : "데이터가 없습니다.",
		align         : "center",
		verticalAlign : "middle",
		style         : {
			fontSize : "2.4rem"
		}
	}, dataLabels : {
		enabled : false
	}
	, stroke      : {
		width : 1
	}
};

const options2 = {
	series        : [],
	title         : {
		text : account + " 장부금액"
	}, chart      : {
		zoom          : {
			enabled : false
		},
		type          : "area",
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
			show : false

		}
	}, tooltip    : {
		enabled : true,
		x       : {
			show   : true,
			format : "MM/dd",
		}
	}, xaxis      : {
		type   : "datetime",
		labels : {
			datetimeFormatter : {
				year  : "yyyy년",
				month : "MM월 dd일",
				day   : "MM월 dd일"
			}
		}
	}, yaxis      : {
		tooltip : {
			enabled : true,
		}, labels : {
		formatter : function (val) {
			if(typeof val === "number") {
				return val.toFixed(0).replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
			}
			return val;
		}
	}
	}, noData     : {
		text          : "데이터가 없습니다.",
		align         : "center",
		verticalAlign : "middle",
		style         : {
			fontSize : "2.4rem"
		}
	}, dataLabels : {
		enabled : false
	}
	, stroke      : {
		width : 1
	}
};

const chart = new ApexCharts(document.querySelector("#chart-area"), options);
chart.render();

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


const chart2 = new ApexCharts(document.querySelector("#account-chart"), options2);
chart2.render();


let chartUrl2 = "/api/data/index/chart/account/" + account;

$.getJSON(chartUrl2, function (response) {
	let dataList = [];

	response.forEach((item) => {
		dataList.push([item.date, item.acc_value]);
	});

	chart2.updateSeries([{
		name : account,
		data : dataList
	}]);
});


