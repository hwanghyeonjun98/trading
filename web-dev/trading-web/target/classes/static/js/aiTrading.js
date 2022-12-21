function aiTrading() {
	$.ajax({
		type    : "POST",
		url     : "/api/data/aiTradingData",
		dataset : "json",
		success : function (trading) {
			console.table(trading);
			// $.each(trading, function (index) {
			// 	console.log();
			// })
		}
	});
}

$(window).on("load", aiTrading);