// 데이터 AJAX로 불러오기 JQUERY 문법 이용

// 버튼 동적 바인딩
$(document).on("click", ".data-view-btn", function () {
	const tableName = $(this).data("table");
	const ajaxUrl = "/api/data/" + tableName + "내역";
	let chartUrl = "/api/data/chart/" + tableName + "내역";
	$.ajax({
		type    : "POST",
		url     : ajaxUrl,
		dataset : "json",
		success : function (reponse) {
			console.log("통신 성공");
			$("#data-table tbody tr").remove();
			$.each(reponse, function (i) {
				str = "<tr><td>" +
				      reponse[i].dates +
				      "</td><td>" +
				      reponse[i].closes +
				      "</td><td>" +
				      reponse[i].opens +
				      "</td><td>" +
				      reponse[i].highs +
				      "</td><td>" +
				      reponse[i].lows +
				      "</td><td>" +
				      reponse[i].volumes +
				      "</td><td>" +
				      reponse[i].changes +
				      "</td></tr>";
				$("#data-table tbody").append(str);
			});
			$("#data-table").attr("data-table", tableName);
		},
		error   : function () {
			console.log("실패");
		}
	});

	// 차트 AJAX
	$.getJSON(chartUrl, function (response) {
		let dataList = [];

		response.forEach((item) => {
			dataList.push([item.dates, item.opens, item.highs, item.lows, item.closes]);
		});

		chart.updateSeries([{
			name : "table",
			data : dataList
		}]);
	});

});