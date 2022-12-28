const time = new Date();
const nowMin = time.getHours() * 60;
const account = $("#account").val();
const tradingDataTableBdoy = $("#trading-data-table tbody");
const histoyTableBody = $("#histoyTable tbody");

// 실기간 트레이딩
if (account !== "") {
	// 장 시작, 끝 시간 이후 메세지 표시
	if (nowMin < 570 || nowMin > 932) {
		tradingDataTableBdoy.html("<tr><td colspan='7'>종료되었습니다.</td></tr>");
	} else {
		(function poll() {
			$.ajax({
				type       : "POST",
				url        : "/api/data/aiTradingData/" + account,
				dataset    : "json",
				success    : function (trading) {
					const list = [];
					$.each(trading, function (index) {
						str = "<tr>" +
						      "<td>" +
						      "<button type='button' id='" + trading[index].code + "_history' data-bs-toggle='modal' data-bs-target='#histoyModal'>"
						      + trading[index].code +
						      "</button>" +
						      "</td>" +
						      "<td>" + trading[index].name + "</td>" +
						      "<td>" + trading[index].amount + "</td>" +
						      "<td>" + trading[index].buyprice + "</td>" +
						      "<td>" + trading[index].evalValue + "</td>" +
						      "<td>" + trading[index].ratio + "</td>" +
						      "<td>" + trading[index].currentValue + "</td>" +
						      "</tr>";
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
				}, 2000),
				error      : function () {
					clearTimeout(poll);
					tradingDataTableBdoy.html("<tr><td colspan='7'>로그인해주세요.</td></tr>");
				}
			});
		})();
	}
} else {
	tradingDataTableBdoy.html("<tr><td colspan='7'>로그인 시 활성화 됩니다.</td></tr>");
}


// 거래 내역 가져오기
$(document).on("click", "#trading-data-table button", function () {
	let url = "/api/data/accountHistory/" + account + "/" + $(this).attr("id").replace("_history", "");
	let code = $(this).attr("id").replace("_history", "");
	$("#stockCode").text(code);

	$.ajax({
		type     : "POST",
		url      : url,
		dataset  : "JSON",
		success  : function (history) {
			let historyList = [];
			$.each(history, function (idx) {
				str = "<tr>" +
				      "<td>" + history[idx].his_time + "</td>" +
				      "<td>" + history[idx].stock_code + "</td>" +
				      "<td>" + history[idx].buy_num + "</td>" +
				      "<td>" + history[idx].sell_num + "</td>" +
				      "</tr>";
				historyList.push(str);
			});
			histoyTableBody.html(historyList);
			if (historyList.length === 0) {
				histoyTableBody.html("<tr><td colspan='4'>거래 내역이 없습니다.</td></tr>");
			}
		}, error : function () {
			histoyTableBody.html("<tr><td colspan='4'>거래 내역이 없습니다.</td></tr>");
		}
	});
});
