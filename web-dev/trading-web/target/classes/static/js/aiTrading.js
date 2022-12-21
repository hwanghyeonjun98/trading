(function poll() {
	$.ajax({
		type       : "POST",
		url        : "/api/data/aiTradingData", // 현재 더미 데이터
		dataset    : "json",
		success    : function (trading) {
			const list = [];
			$.each(trading, function (index) {
				str = "<tr>" +
				      "<td>" + trading[index].stock_code + "</td>" +
				      "<td>" + trading[index].stock_name + "</td>" +
				      "<td>" + trading[index].quantity + "</td>" +
				      "<td>" + trading[index].average_price + "</td>" +
				      "<td>" + trading[index].appraisal_amount + "</td>" +
				      "<td>" + trading[index].returns + "</td>" +
				      "<td>" + trading[index].book_value + "</td>" +
				      "</tr>";
				list.push(str);
			});
			if (list.length === 0) {
				$("#trading-data-table tbody").html("<tr><td colspan='7'>현재는 장중이 아닙니다.</td></tr>");
			} else {
				$("#trading-data-table tbody").html(list);
			}
		}, timeout : 5000,
		complete   : setTimeout(function () {
			poll();
		}, 5000)
	});
})();

