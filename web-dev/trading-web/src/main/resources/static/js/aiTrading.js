const time = new Date();
const nowMin = time.getHours() * 60;
const account = $("#account").val();

if (nowMin < 570 || nowMin > 930) {
	console.log(nowMin);
	$("#trading-data-table tbody").html("<tr><td colspan='7'>종료되었습니다.</td></tr>");
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
			}, timeout : 2000,
			complete   : setTimeout(function () {
				poll();


			}, 2000),
			error      : function () {
				clearTimeout(poll);
				$("#trading-data-table tbody").html("<tr><td colspan='7'>로그인해주세요.</td></tr>");
			}
		});
	})();
}

