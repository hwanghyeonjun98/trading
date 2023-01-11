let fsList = [];
let fsInfo = [];

const search = $("#fsData").val();
const modalBtn = document.querySelector("#fsModalBtn");
const modal = document.querySelector("#fsmodal");

$(window).on("load", function () {
	$.ajax({
		type    : "POST",
		url     : "/api/data/fsList",
		dataset : "json",
		success : function (list) {
			$.each(list, function (idx) {
				str = "<option value='" + list[idx].stockCode + "'>" +
				      "<span>" + list[idx].stockCode + " </span>" +
				      "<span>" + list[idx].korName + " </span>" +
				      "<span>" + list[idx].korAbbrvName + " </span>" +
				      "<span>" + list[idx].engName + " </span>" +
				      "<span>" + list[idx].mrkCls + " </span>" +
				      "<span>" + list[idx].scrCls + " </span>" +
				      "<span>" + list[idx].stockType + "</span>" +
				      "</option>";
				fsList.push(str);
			});

			$("#fs-data-list").html(fsList);
			return fsList;
		},
		error   : function () {
			return false;
		}
	});
});

$("#fsData").on("keyup", function (event) {
	if (event.keyCode !== 13) {
		fsList.fill(search);
	}
});


$("#fsModalBtn").on("click", function () {
	const search = $("#fsData").val();

	if (fsInfo <= 0) {
		$.ajax({
			type     : "POST",
			url      : "/api/data/fsInfo/" + search,
			dataset  : "json",
			success  : function (respense) {
				$.each(respense, function (idx) {
					str = "<tr>" +
					      "<td>" + respense[idx].날짜 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_유동자산 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_비유동자산 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_자산총계 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_유동부채 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_비유동부채 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_부채총계 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_자본금 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_이익잉여금 + "</td>" +
					      "<td>" + respense[idx].재무제표_재무상태표_자본총계 + "</td>" +
					      "<td>" + respense[idx].재무제표_손익계산서_매출액 + "</td>" +
					      "<td>" + respense[idx].재무제표_손익계산서_영업이익 + "</td>" +
					      "<td>" + respense[idx].재무제표_손익계산서_법인세차감전_순이익 + "</td>" +
					      "<td>" + respense[idx].재무제표_손익계산서_당기순이익 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_유동자산 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_비유동자산 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_자산총계 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_유동부채 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_비유동부채 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_부채총계 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_자본금 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_이익잉여금 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_재무상태표_자본총계 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_손익계산서_매출액 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_손익계산서_영업이익 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_손익계산서_법인세차감전_순이익 + "</td>" +
					      "<td>" + respense[idx].연결재무제표_손익계산서_당기순이익 + "</td>" +
					      "</tr>";
					fsInfo.push(str);
				});
				$("#fsTable tbody").html();
				return fsInfo;
			},
			complete : function () {
				$(".loading-div").addClass("active");
				$("#fsTable tbody").html(fsInfo);
			},
			error    : function () {
				$("#fsTable tbody").html("<tr><td colspan='8'>정보가 없습니다.</td></tr>");
			}
		});
	} else {
		$(".loading-div").addClass("active");
		$("#fsTable tbody").html("<tr><td colspan='8'>정보가 없습니다.</td></tr>");
	}
});

$(".modal-close").on("click", function () {
	$(".loading-div").removeClass("active");
});