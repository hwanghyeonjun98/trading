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
				year  : "yyyy",
				month : "MM/dd",
				day   : "MM/dd"
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

// 어제 날짜 지정
date = new Date();
date.setDate(date.getDate() - 1);
const yesterday = new Intl.DateTimeFormat("ko", {dateStyle : "long"}).format(date);

const options2 = {
	series        : [],
	title         : {
		text    : account + " 수익률 비교",
		offsetY : 18,
		style   : {
			fontSize     : "1.4rem",
			margin       : "0",
			borderBottom : "1px solid #000"
		}
	}, subtitle   : {
		text : yesterday + " 기준 (단위 : %)",
	}, chart      : {
		zoom          : {
			enabled : true
		},
		type          : "line",
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
			show    : true,
			offsetY : 26,
			export  : {
				csv : {
					filename : nowDate + "_" + account + "_수익률비교",
					dateFormatter(timestamp) {
						return timestamp;
					}
				},
				png : {
					filename : nowDate + "_" + account + "_수익률비교",
				},
				svg : {
					filename : nowDate + "_" + account + "_수익률비교",
				}
			}
		}
	}, tooltip    : {
		enabled : true,
		x       : {
			show   : true,
			format : "yyyy/MM/dd",
		}
	}, xaxis      : {
		type   : "datetime",
		labels : {
			datetimeFormatter : {
				year  : "yyyy",
				month : "MM/dd",
				day   : "MM/dd"
			}
		}
	}, yaxis      : {
		tooltip   : {
			enabled : true,
		}, labels : {
			formatter : function (val) {
				if (typeof val === "number") {
					return val.toFixed(2).replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
				}
				return val;
			}
		}
	}, noData     : {
		text          : "데이터가 없습니다.",
		align         : "center",
		verticalAlign : "middle",
		style         : {
			fontSize  : "1.8 rem",
			textAlign : "center"
		}
	}, dataLabels : {
		enabled : false
	}, stroke     : {
		width : 2
	}, markers    : {
		size  : [6, 6],
		hover : {
			size       : 7,
			sizeOffset : 3
		}
	}
};

const options3 = {
	series        : [],
	title         : {
		text    : account + " 장부 금액",
		offsetY : 18,
		style   : {
			fontSize     : "1.4rem",
			margin       : "0",
			borderBottom : "1px solid #000"
		}
	}, subtitle   : {
		text : "(단위 : 백만원)",
	}, chart      : {
		zoom          : {
			enabled : true
		},
		type          : "line",
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
			show    : true,
			offsetY : 26,
			export  : {
				csv : {
					filename : nowDate + "_" + account + "_장부금액",
					dateFormatter(timestamp) {
						return timestamp;
					}
				},
				png : {
					filename : nowDate + "_" + account + "_장부금액",
				},
				svg : {
					filename : nowDate + "_" + account + "_장부금액",
				}
			}
		}
	}, tooltip    : {
		enabled : true,
		x       : {
			show   : true,
			format : "yyyy/MM/dd",
		}
	}, xaxis      : {
		type   : "datetime",
		labels : {
			datetimeFormatter : {
				year  : "yyyy/",
				month : "MM/dd",
				day   : "MM/dd"
			}
		}
	}, yaxis      : {
		tooltip   : {
			enabled : true,
		}, labels : {
			formatter : function (val) {
				if (typeof val === "number") {
					return val.toFixed(2).replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
				}
				return val;
			}
		}
	}, noData     : {
		text          : "데이터가 없습니다.",
		align         : "center",
		verticalAlign : "middle",
		style         : {
			fontSize  : "1.8 rem",
			textAlign : "center"
		}
	}, dataLabels : {
		enabled : false
	}, stroke     : {
		width : 2
	}, markers    : {
		size  : [6, 6],
		hover : {
			size       : 7,
			sizeOffset : 3
		}
	}
};

const kospiChart = new ApexCharts(document.querySelector("#chart-area"), options);
kospiChart.render();

let kospiChartUrl = "/api/data/index/chart/kospi";

$.getJSON(kospiChartUrl, function (response) {
	let dataList = [];

	response.forEach((item) => {
		dataList.push([item.dates, item.closes]);
	});

	kospiChart.updateSeries([{
		name : "KOSPI",
		data : dataList
	}]);
});


const ratioChart = new ApexCharts(document.querySelector("#ratio-chart"), options2);
ratioChart.render();

let ratioChartUrl = "/api/data/index/chart/account/ratio/" + account;

$.getJSON(ratioChartUrl, function (response) {
	let ratioDateList = [];
	let accValueList = [];
	let ratioList = [];
	let kospiList = [];
	let kosdaqList = [];

	response.forEach((item) => {
		ratioDateList.push(item.date);
		accValueList.push(item.acc_value);
		kospiList.push([item.date, item.kospi_changes]);
		kosdaqList.push([item.date, item.kosdaq_changes]);
	});

	for (let i = 0; i < accValueList.length; i++) {
		let num1 = accValueList[i];
		let num2 = accValueList[i + 1];
		let num = (num2 - num1) / num1 * 100;
		ratioList.push(num);
	}

	ratioList.unshift(0);

	let ratioSeries = [];

	for (let i = 0; i < accValueList.length; i++) {
		ratioSeries.push([ratioDateList[i], ratioList[i]]);
	}

	kospiList[0][1] = "0";
	kosdaqList[0][1] = "0";

	ratioChart.updateSeries([{
		name : "내 계좌",
		data : ratioSeries
	}, {
		name : "KOSPI",
		data : kospiList
	}, {
		name : "KOSDAQ",
		data : kosdaqList
	}]);
});

const accountChart = new ApexCharts(document.querySelector("#account-chart"), options3);
accountChart.render();

let accountChartUrl = "/api/data/index/chart/account/" + account;

$.getJSON(accountChartUrl, function (response) {
	let accountList = [];
	response.forEach((item) => {
		accountList.push([item.date, item.acc_value / 1000000]);
	});

	accountChart.updateSeries([{
		name : account,
		data : accountList
	}]);
});

const accViewBtn = document.querySelector(".account-chart-view-btn");
const accViewArea = document.querySelector(".account-chart-area");
accViewBtn.addEventListener("click", () => {
	accViewArea.classList.toggle("active");
	if (accViewArea.classList.contains("active")) {
		accViewBtn.innerText = "닫기";
	} else {
		accViewBtn.innerText = "장부금액 보기";
	}
});


