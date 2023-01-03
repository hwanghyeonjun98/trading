/**
 * 차트리트스 옵션
 * [자세한 설정은 https://apexcharts.com/docs/installation/ 참고]
 * series : X, Y축 값 설정
 * chart : 차트 종류, 기본값 설정
 * tooltip : 마우스 올렸을 때 상세 내용 설정
 * xaxis : X축 설정
 * yaxis : Y축 설정
 * plotOptions : 축 색깔 설정
 * noData : 데이터가 없을 때 설정(데이터 없음 문구 같은거)
 */

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
				reset    : "<i class=\"bi bi-arrow-counterclockwise\" style=\"font-size:20px;\"></i>"
			}
		}
	}, tooltip     : {
		enabled   : true,
		x         : {
			show   : true,
			format : "MM/dd",
		}, custom : function ({seriesIndex, dataPointIndex, w}) {
			let o = w.globals.seriesCandleO[seriesIndex][dataPointIndex].toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
			let h = w.globals.seriesCandleH[seriesIndex][dataPointIndex].toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
			let l = w.globals.seriesCandleL[seriesIndex][dataPointIndex].toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
			let c = w.globals.seriesCandleC[seriesIndex][dataPointIndex].toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
			return (
				"<div class=\"apexcharts-tooltip-box apexcharts-tooltip-candlestick\">" +
				"<div>시가: <span class=\"value\">" +
				o +
				"</span></div>" +
				"<div>고가: <span class=\"value\">" +
				h +
				"</span></div>" +
				"<div>저가: <span class=\"value\">" +
				l +
				"</span></div>" +
				"<div>종가: <span class=\"value\">" +
				c +
				"</span></div>" +
				"</div>"
			);
		}
	}, xaxis       : {
		type          : "datetime",
		tickPlacement : "on",
		labels        : {
			datetimeFormatter : {
				year  : "yyyy년",
				month : "MM월 dd일",
				day   : "MM월 dd일"
			}
		}
	}, yaxis       : {
		tooltip   : {
			enabled : true,
		}, labels : {
			formatter : function (val) {
				if(typeof val === "number") {
					return val.toFixed(2).replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
				}
				return val;
			}
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


// 차트 object 생성
const chart = new ApexCharts(document.querySelector("#chart-area"), options);
// 차트 랜더딩
chart.render();



