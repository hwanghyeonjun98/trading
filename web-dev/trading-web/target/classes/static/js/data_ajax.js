// 데이터 AJAX로 불러오기 JQUERY 문법 이용

// 윈도우 로드 시 차트 가져오기
$(window).on("load", function () {
	const nowUrl = decodeURI(window.location.href);
	let name = nowUrl.split("/");
	name = name[name.length - 1];

	let chartUrl;
	if (name === "data") {
		chartUrl = "/api/data/chart/aedkrw내역";
	} else {
		chartUrl = "/api/data/chart/" + name + "내역";
	}

	// 차트 AJAX
	$.getJSON(chartUrl, function (response) {
		let dataList = [];

		// 차트 리스트 만들기
		response.forEach((item) => {
			dataList.push([item.dates, item.opens, item.highs, item.lows, item.closes]);
		});

		// 차트 옵션 series 업데이트 메소드
		chart.updateSeries([{
			name : "table",
			data : dataList
		}]);
	});
});

// 날짜 검색 관련
$(document).on("submit", "form[name=dateSearchFrm]", function (event) { // 폼전송 코드
                                                                        // 폼 전송 이벤트 초기화(새로고침 안되게)
	event.preventDefault();

	// 폼안에 날짜 가져오기
	let startDate = $("#startDate").val();
	let endDate = $("#endDate").val();
	startDate = startDate.replaceAll("-", "");
	endDate = endDate.replaceAll("-", "");

	const tableName = $("#data-table").data("table"); // 테이블에서 data-table 이름 가져오기
	const searchUrl = "/api/data/dateSearch/" + tableName + "내역/" + startDate + "/" + endDate; // API URL

	// 예외 처리
	const searchError = "<tr><td colspan='7' class='text-center'>데이터가 없습니다. 날짜를 확인 해주세요.</td></tr>";
	$.ajax({
		type    : "POST", // GET, POST, PUT, DELETE
		url     : searchUrl,
		dataset : "json", // 데이터 타입, JSON or XML (HTML도 되지만 사용 지양)
		success : function (reponse) { // 통신 성공시 진행하는 코드
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
		},
		error   : function () { // 통신 실패시 진행하는 코드
			console.log("실패");
			$("#data-table tbody").append(searchError);
		}
	});
});