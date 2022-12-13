// 데이터 AJAX로 불러오기 JQUERY 문법 이용

// 윈도우 로드 시 차트 가져오기
$(window).on("load", function () {
	const nowUrl = decodeURI(window.location.href);
	let name = nowUrl.split("/");
	name = name[name.length - 1];

	let chartUrl = "/api/data/chart/" + name + "내역";

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

// 날짜 검색 관련
$(document).on("submit", "form[name=dateSearchFrm]", function (event) {
	event.preventDefault();

	let startDate = $("#startDate").val();
	let endDate = $("#endDate").val();
	startDate = startDate.replaceAll("-", "");
	endDate = endDate.replaceAll("-", "");

	const tableName = $("#data-table").data("table");
	const searchUrl = "/api/data/dateSearch/" + tableName + "내역/" + startDate + "/" + endDate;

	// 예외 처리
	const nothing = "<tr><td colspan='7' class='text-center'>데이터가 없습니다.</td></tr>";
	const searchError = "<tr><td colspan='7' class='text-center'>날짜를 확인 해주세요.</td></tr>";
	$.ajax({
		type    : "POST",
		url     : searchUrl,
		dataset : "json",
		success : function (reponse) {
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
				      "%</td></tr>";
				$("#data-table tbody").append(str);
			});
			$("#data-table").attr("data-table", tableName);

			if ($("#data-table tbody tr").length === 0) {
				$("#data-table tbody").append(nothing);
			}
		},
		error   : function () {
			console.log("실패");
			$("#data-table tbody").append(searchError);
		}
	});
});