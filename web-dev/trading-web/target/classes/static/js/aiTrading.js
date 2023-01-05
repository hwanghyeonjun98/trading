const tradingDataTableBdoy = $("#trading-data-table tbody");
date = new Date(); // 사간 초기화
const nowMin = date.getHours() * 60;

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

					if(trading[index].code !== "0") {
						list.push(str);
					}
				});
				if (list.length === 0) {
					tradingDataTableBdoy.html("<tr><td colspan='7'>거래중입니다. 잠시만 기다려주세요.</td></tr>");
				} else {
					tradingDataTableBdoy.html(list);
				}
			}, timeout : 10000,
			complete   : setTimeout(function () {
				poll();
			}, 5000),
			error      : function () {
				clearTimeout(poll);
				tradingDataTableBdoy.html("<tr><td colspan='7'>데이터가 없습니다.</td></tr>");
			}
		});
	})();
	}
} else {
	tradingDataTableBdoy.html("<tr><td colspan='7'>로그인 시 활성화 됩니다.<br>로그인해주세요.</td></tr>");
}