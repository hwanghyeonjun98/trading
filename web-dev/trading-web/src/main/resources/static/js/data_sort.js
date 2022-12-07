$(document).on("click", ".sort-btn", function () {
	const tableName = $("#data-table").data("table");
	const base = $(this).parent().attr("class");

	let startDate = $("#startDate").val();
	let endDate = $("#endDate").val();
	startDate = startDate.replaceAll("-", "");
	endDate = endDate.replaceAll("-", "");

	let sortUrl;
	if (!$(this).hasClass("sorted")) {
		$(".sort-btn").removeClass("sorted");
		$(this).addClass("sorted");
		sortUrl = "/api/data/sorts/" + tableName + "내역/" + base + "/asc/" + startDate + "/" + endDate;
	} else {
		$(this).removeClass("sorted");
		sortUrl = "/api/data/sorts/" + tableName + "내역/" + base + "/desc/" + startDate + "/" + endDate;
	}
	$.ajax({
		type    : "POST",
		url     : sortUrl,
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
		},
		error   : function () {
			console.log("실패");
		}
	});
});