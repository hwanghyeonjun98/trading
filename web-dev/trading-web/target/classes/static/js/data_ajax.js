$(document).on("click", ".data-view-btn", function () {
	const tableName = $(this).text();
	const ajaxUrl = "/api/data/" + tableName;
	$.ajax({
		type    : "POST",
		url     : ajaxUrl,
		dataset : "json",
		success : function (data) {
			console.log("통신 성공");
			$.each(data, function (i) {
				str = "<tr><td>" +
				      data[i].dates +
				      "</td><td>" +
				      data[i].closes +
				      "</td><td>" +
				      data[i].opens +
				      "</td><td>" +
				      data[i].highs +
				      "</td><td>" +
				      data[i].lows +
				      "</td><td>" +
				      data[i].volumes +
				      "</td><td>" +
				      data[i].changes +
				      "</td></tr>";
				$("#data-table tbody").append(str);
			});
			$("#data-table").attr("data-table", tableName);
		},
		error   : function () {
			console.log("실패");
		}
	});
});

