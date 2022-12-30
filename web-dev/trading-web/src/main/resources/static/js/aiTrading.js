const account = $("#account").val();
const tradingDataTableBdoy = $("#trading-data-table tbody");
const histoyTableBody = $("#histoyTable tbody");
const allHistoyTableBody = $("#allHistoyTable tbody");
const coList = $(".history-list");

// 실기간 트레이딩
if (account !== "") {
	// 장 시작, 끝 시간 이후 메세지 표시
	// if (nowMin < 570 || nowMin > 932) {
	// 	tradingDataTableBdoy.html("<tr><td colspan='7'>종료되었습니다.</td></tr>");
	// } else {
	(function poll() {
		$.ajax({
			type       : "POST",
			url        : "/api/data/aiTradingData/" + account,
			dataset    : "json",
			success    : function (trading) {
				const list = [];
				$.each(trading, function (index) {
					let ratio = trading[index].ratio;
					let evalValue = trading[index].evalValue;

					str1 = "<tr>" +
					       "<td>" +
					       "<button type='button' id='" + trading[index].code + "_history' data-bs-toggle='modal' data-bs-target='#histoyModal'>"
					       + trading[index].code +
					       "</button>" +
					       "</td>" +
					       "<td>" + trading[index].name + "</td>" +
					       "<td>" + trading[index].amount + "</td>" +
					       "<td>" + trading[index].buyprice + "</td>";

					if (ratio < 0) {
						str2 = "<td class='stock-evalValue down'>" + evalValue + "</td>" +
						       "<td class='stock-ratio down'>" + ratio + "</td>";
					} else {
						str2 = "<td class='stock-evalValue up'>" + evalValue + "</td>" +
						       "<td class='stock-ratio up'>" + ratio + "</td>";
					}

					str3 = "<td>" + trading[index].currentValue + "</td>" +
					       "</tr>";

					str = str1 + str2 + str3;
					list.push(str);
				});
				if (list.length === 0) {
					tradingDataTableBdoy.html("<tr><td colspan='7'>거래중입니다. 잠시만 기다려주세요.</td></tr>");
				} else {
					tradingDataTableBdoy.html(list);
				}
			}, timeout : 5000,
			complete   : setTimeout(function () {
				poll();
			}, 20000),
			error      : function () {
				clearTimeout(poll);
				tradingDataTableBdoy.html("<tr><td colspan='7'>데이터가 없습니다.</td></tr>");
			}
		});
	})();
	// }
} else {
	tradingDataTableBdoy.html("<tr><td colspan='7'>로그인 시 활성화 됩니다.<br>로그인해주세요.</td></tr>");
}

// 거래 내역 가져오기
$(document).on("click", "#trading-data-table button", function () {
	let url = "/api/data/accountHistory/" + account + "/" + $(this).text();
	let stockCode = $(this).attr("id").replace("_history", "");
	let stockName = $(this).parent().next().text();

	$("#stockCode").text(stockCode);
	$("#stockName").text(stockName);

	$.ajax({
		type     : "POST",
		url      : url,
		dataset  : "JSON",
		success  : function (history) {
			let historyList = [];
			$.each(history, function (idx) {
				if (history[idx].profit < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + history[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].amount + "</td>" +
					      "<td class='color-blue'>" + history[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + history[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + history[idx].his_time + "</td>" +
					      "<td class='color-red'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + history[idx].amount + "</td>" +
					      "<td class='color-red'>" + history[idx].ratio + "</td>" +
					      "<td class='color-red'>" + history[idx].profit + "</td>" +
					      "</tr>";
				}
				historyList.push(str);
			});
			histoyTableBody.html(historyList);
			if (historyList.length === 0) {
				histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
			}
		}, error : function () {
			histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
		}
	});
});

// 낧짜 검색
$(document).on("submit", "form[name=codeSearchFrm]", function (event) {
	event.preventDefault();

	let startDate = $("#startDate").val();
	let endDate = $("#endDate").val();
	startDate = startDate.replace("T", " ");
	endDate = endDate.replace("T", " ");

	const stockCode = $("#stockCode").text();

	const searchUrl = "/api/data/accountHistorySearch/" + account + "/" + stockCode + "/" + startDate + "/" + endDate;

	// 예외 처리
	const searchError = "<tr><td colspan='6' class='text-center'>데이터가 없습니다. 날짜를 확인 해주세요.</td></tr>";
	$.ajax({
		type     : "POST",
		url      : searchUrl,
		dataset  : "json",
		success  : function (reponse) {
			let dataList = [];
			$.each(reponse, function (idx) {
				if(parseInt(history[idx].profit) < 0){
					str = "<tr>" +
					      "<td class='color-blue'>" + history[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].amount + "</td>" +
					      "<td class='color-blue'>" + history[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + history[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + history[idx].his_time + "</td>" +
					      "<td class='color-red'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + history[idx].amount + "</td>" +
					      "<td class='color-red'>" + history[idx].ratio + "</td>" +
					      "<td class='color-red'>" + history[idx].profit + "</td>" +
					      "</tr>";
				}
				dataList.push(str);
			});
			histoyTableBody.html(dataList);
		}, error : function () {
			console.log("실패");
			histoyTableBody.html(searchError);
		}
	});
});

$(document).on("click", "#all-history-btn", function () {
	let url = "/api/data/allHistoryData/" + account;

	$.ajax({
		type     : "POST",
		url      : url,
		dataset  : "JSON",
		success  : function (history) {
			let allHistoryList = [];
			$.each(history, function (idx) {
				if (parseInt(history[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + history[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + history[idx].code_name + "</td>" +
					      "<td class='color-blue'>" + history[idx].stock_code + "</td>" +
					      "<td class='color-blue'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].amount + "</td>" +
					      "<td class='color-blue'>" + history[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + history[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + history[idx].his_time + "</td>" +
					      "<td class='color-red'>" + history[idx].code_name + "</td>" +
					      "<td class='color-red'>" + history[idx].stock_code + "</td>" +
					      "<td class='color-red'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + history[idx].amount + "</td>" +
					      "<td class='color-red'>" + history[idx].ratio + "</td>" +
					      "<td class='color-red'>" + history[idx].profit + "</td>" +
					      "</tr>";
				}
				allHistoryList.push(str);
			});
			allHistoyTableBody.html(allHistoryList);
			if (allHistoryList.length === 0) {
				allHistoyTableBody.html("<tr><td colspan='8'>거래 내역이 없습니다.</td></tr>");
			}
		}, error : function () {
			allHistoyTableBody.html("<tr><td colspan='8'>거래 내역이 없습니다.</td></tr>");
		}
	});
});

$(document).on("submit", "form[name=allSearchFrm]", function (event) {
	event.preventDefault();

	let code = $("#code").val();
	if (code === "") {
		code = "null";
	}

	let startDate = $("#startDate2").val();
	let endDate = $("#endDate2").val();
	startDate = startDate.replace("T", " ");
	endDate = endDate.replace("T", " ");

	let searchUrl = "/api/data/allHistoryDataSearch/" + account + "/" + startDate + "/" + endDate + "/" + code;

	// 예외 처리
	const searchError = "<tr><td colspan='8' class='text-center'>데이터가 없습니다. 날짜를 확인 해주세요.</td></tr>";
	$.ajax({
		type     : "POST",
		url      : searchUrl,
		dataset  : "json",
		success  : function (reponse) {
			let allDataList = [];
			$.each(reponse, function (idx) {
				if (parseInt(reponse[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + reponse[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].code_name + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].stock_code + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].amount + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + reponse[idx].his_time + "</td>" +
					      "<td class='color-red'>" + reponse[idx].code_name + "</td>" +
					      "<td class='color-red'>" + reponse[idx].stock_code + "</td>" +
					      "<td class='color-red'>" + reponse[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + reponse[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + reponse[idx].amount + "</td>" +
					      "<td class='color-red'>" + reponse[idx].ratio + "</td>" +
					      "<td class='color-red'>" + reponse[idx].profit + "</td>" +
					      "</tr>";
				}
				allDataList.push(str);
			});
			allHistoyTableBody.html(allDataList);
		}, error : function () {
			console.log("실패");
			allHistoyTableBody.html(searchError);
		}
	});
});

$(window).on("load", function () {
	// 현재 날짜 가져오기
	const date = new Date();
	const today = new Intl.DateTimeFormat("kr", {dateStyle : "full"}).format(date);

	$(".historyDate").text(today);

	let errorMsg = "<li>거래된 회사가 없습니다.</li>";
	$.ajax({
		type     : "POST",
		url      : "/api/data/coList/" + account,
		dataset  : "json",
		success  : function (list) {
			let companyList = [];
			$.each(list, function (idx) {
				str = "<li>" +
				      "<button type='button' class='btn' data-stock-code='" + list[idx].stock_code + "' data-bs-toggle='modal' data-bs-target='#histoyModal'>" +
				      list[idx].code_name +
				      "</button>" +
				      "</li>";
				companyList.push(str);
			});
			coList.html(companyList);
			if (companyList.length === 0) {
				coList.html(errorMsg);
			}
		}, error : function () {
			coList.html(errorMsg);
		}
	});
});

$(document).on("click", ".history-list button", function () {
	let url = "/api/data/coListSearch/" + account + "/" + $(this).data("stock-code");

	let stockCode = $(this).data("stock-code");
	let stockName = $(this).text();

	$("#stockCode").text(stockCode);
	$("#stockName").text(stockName);

	$.ajax({
		type     : "POST",
		url      : url,
		dataset  : "JSON",
		success  : function (history) {
			let historyList = [];
			$.each(history, function (idx) {
				if (parseInt(history[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + history[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].amount + "</td>" +
					      "<td class='color-blue'>" + history[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + history[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + history[idx].his_time + "</td>" +
					      "<td class='color-red'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + history[idx].amount + "</td>" +
					      "<td class='color-red'>" + history[idx].ratio + "</td>" +
					      "<td class='color-red'>" + history[idx].profit + "</td>" +
					      "</tr>";
				}
				historyList.push(str);
			});
			histoyTableBody.html(historyList);
			if (historyList.length === 0) {
				histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
			}
		}, error : function () {
			histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
		}
	});
});
