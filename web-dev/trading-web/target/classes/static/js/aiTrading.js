(function poll() {
	$.ajax({
		type       : "POST",
		url        : "/api/data/aiTradingData", // 현재 더미 데이터
		dataset    : "json",
		success    : function (trading) {
			const list = [];
			$.each(trading, function (index) {
				str = "<tr>" +
				      "<td>" + trading[index].code + "</td>" +
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
				$("#trading-data-table tbody").html("<tr><td colspan='7'>거래중입니다. 잠시만 기다려주세요.</td></tr>");
			} else {
				$("#trading-data-table tbody").html(list);
			}
		}, timeout : 8000,
		complete   : setTimeout(function () {
			poll();
		}, 8000),
		error: function () {
			$("#trading-data-table tbody").html("<tr><td colspan='7'>현재 장중이 아니거나<br>데이터가 없습니다.</td></tr>");
		}
	});
})();

