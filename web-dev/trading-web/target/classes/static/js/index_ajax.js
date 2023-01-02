const account = $("#account").val();
const histoyTableBody = $("#histoyTable tbody");
const allHistoyTableBody = $("#allHistoyTable tbody");
const coList = $(".history-list");

(function ranking() {
	$.ajax({
		type       : "POST",
		url        : "/api/data/marketCapRanking",
		dataset    : "json",
		success    : function (ranking) {
			const list = [];
			$.each(ranking, function (index) {
				str
					= "<li>" + ranking[index].no + ". " + ranking[index].stock_name + " (" + ranking[index].market_cap + ")</li>";
				list.push(str);
			});
			$("#rolling").html(list);
		}, timeout : 60000,
		complete   : setTimeout(function () {
			ranking();
		}, 60000),
		error      : function () {
			$("#rolling").html("<li>데이터가 없습니다.</li>");
		}
	});
})();

const rolling = document.getElementById("rolling");

let rollingBanner = setInterval(function () {

	rolling.style.transitionDuration = "1000ms";
	rolling.style.marginTop = "-2em";

	setTimeout(function () {

		rolling.removeAttribute("style");
		rolling.appendChild(rolling.firstElementChild);

	}, 1000);
}, 5000);
rolling.addEventListener("mouseenter", () => {
	console.log("마우스 올림");
	clearInterval(rollingBanner);
});

rolling.addEventListener("mouseleave", () => {
	rollingBanner = setInterval(function () {

		rolling.style.transitionDuration = "1000ms";
		rolling.style.marginTop = "-2em";

		setTimeout(function () {

			rolling.removeAttribute("style");
			rolling.appendChild(rolling.firstElementChild);

		}, 1000);
	}, 5000);
});

const defaultDate = new Date();
document.querySelector("#current").innerHTML = defaultDate.toLocaleTimeString();

setInterval(displayNow, 1000); // 1초마다 시간 갱신
function displayNow() {
	const now = new Date();
	document.querySelector("#current").innerHTML = now.toLocaleTimeString();
}

// 거래 내역 가져오기
$(document).on("click", "#trading-data-table button", function () {
	let url = "/api/data/accountHistory/" + account + "/" + $(this).text();
	let stockCode = $(this).attr("id").replace("_history", "");
	let stockName = $(this).parent().next().text();

	$("#stockCode").text(stockCode);
	$("#stockName").text(stockName);

	$.ajax({
		type     : "POST",
		url      : url,
		dataset  : "JSON",
		success  : function (history) {
			let historyList = [];
			$.each(history, function (idx) {
				if (parseInt(history[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + history[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].amount + "</td>" +
					      "<td class='color-blue'>" + history[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + history[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + history[idx].his_time + "</td>" +
					      "<td class='color-red'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + history[idx].amount + "</td>" +
					      "<td class='color-red'>" + history[idx].ratio + "</td>" +
					      "<td class='color-red'>" + history[idx].profit + "</td>" +
					      "</tr>";
				}
				historyList.push(str);
			});
			histoyTableBody.html(historyList);
			if (historyList.length === 0) {
				histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
			}
		}, error : function () {
			histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
		}
	});
});

// 낧짜 검색
$(document).on("submit", "form[name=codeSearchFrm]", function (event) {
	event.preventDefault();

	let startDate = $("#startDate").val();
	let endDate = $("#endDate").val();
	startDate = startDate.replace("T", " ");
	endDate = endDate.replace("T", " ");

	const stockCode = $("#stockCode").text();

	const searchUrl = "/api/data/accountHistorySearch/" + account + "/" + stockCode + "/" + startDate + "/" + endDate;

	// 예외 처리
	const searchError = "<tr><td colspan='6' class='text-center'>데이터가 없습니다. 날짜를 확인 해주세요.</td></tr>";
	$.ajax({
		type     : "POST",
		url      : searchUrl,
		dataset  : "json",
		success  : function (reponse) {
			let dataList = [];
			$.each(reponse, function (idx) {
				if (parseInt(reponse[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + reponse[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].amount + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + reponse[idx].his_time + "</td>" +
					      "<td class='color-red'>" + reponse[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + reponse[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + reponse[idx].amount + "</td>" +
					      "<td class='color-red'>" + reponse[idx].ratio + "</td>" +
					      "<td class='color-red'>" + reponse[idx].profit + "</td>" +
					      "</tr>";
				}
				dataList.push(str);
			});
			histoyTableBody.html(dataList);
		}, error : function () {
			console.log("실패");
			histoyTableBody.html(searchError);
		}
	});
});

$(document).on("click", "#all-history-none-btn", function () {
	alert("회원 전용 기능입니다.");
	location.href = "/login";
});

$(document).on("click", "#all-history-btn", function () {
	let url = "/api/data/allHistoryData/" + account;

	$.ajax({
		type     : "POST",
		url      : url,
		dataset  : "JSON",
		success  : function (history) {
			let allHistoryList = [];
			$.each(history, function (idx) {
				if (parseInt(history[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + history[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + history[idx].code_name + "</td>" +
					      "<td class='color-blue'>" + history[idx].stock_code + "</td>" +
					      "<td class='color-blue'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].amount + "</td>" +
					      "<td class='color-blue'>" + history[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + history[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + history[idx].his_time + "</td>" +
					      "<td class='color-red'>" + history[idx].code_name + "</td>" +
					      "<td class='color-red'>" + history[idx].stock_code + "</td>" +
					      "<td class='color-red'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + history[idx].amount + "</td>" +
					      "<td class='color-red'>" + history[idx].ratio + "</td>" +
					      "<td class='color-red'>" + history[idx].profit + "</td>" +
					      "</tr>";
				}
				allHistoryList.push(str);
			});
			allHistoyTableBody.html(allHistoryList);
			if (allHistoryList.length === 0) {
				allHistoyTableBody.html("<tr><td colspan='8'>거래 내역이 없습니다.</td></tr>");
			}
		}, error : function () {
			allHistoyTableBody.html("<tr><td colspan='8'>거래 내역이 없습니다.</td></tr>");
		}
	});

	$.ajax({
		type     : "post",
		url      : "/api/data/profit/" + account,
		dataset  : "json",
		success  : function (rate) {
			if (parseInt(rate[0].profit) < 0) {
				str = "<span class='color-blue fw-bold'>" +
				      "수익율 : " + rate[0].ratio + "%, " +
				      "</span>" +
				      "<span class='color-blue fw-bold'>" +
				      "금액 : " + rate[0].profit + "원 " +
				      "</span>" +
				      "<span class='fw-bold'>(" +
				      nowDate +
				      "</span> 1일 기준)";
			} else {
				str = "<span class='color-red fw-bold'>" +
				      "수익율 : " + rate[0].ratio + "%, " +
				      "</span>" +
				      "<span class='color-red fw-bold'>" +
				      "금액 : " + rate[0].profit + "원 " +
				      "</span>" +
				      "<span class='fw-bold'>(" +
				      nowDate +
				      "</span>)";
			}

			$(".profit-area p").html(str);
		}, error : function () {
			$(".profit-area p").text("정보를 불러오지 못했습니다.");
		}
	});
});

$(document).on("submit", "form[name=allSearchFrm]", function (event) {
	event.preventDefault();

	let code = $("#code").val();
	if (code === "") {
		code = "null";
	}

	let startDate = $("#startDate2").val();
	let endDate = $("#endDate2").val();
	startDate = startDate.replace("T", " ");
	endDate = endDate.replace("T", " ");

	let searchUrl = "/api/data/allHistoryDataSearch/" + account + "/" + startDate + "/" + endDate + "/" + code;

	// 예외 처리
	const searchError = "<tr><td colspan='8' class='text-center'>데이터가 없습니다. 날짜를 확인 해주세요.</td></tr>";
	$.ajax({
		type     : "POST",
		url      : searchUrl,
		dataset  : "json",
		success  : function (reponse) {
			let allDataList = [];
			$.each(reponse, function (idx) {
				if (parseInt(reponse[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + reponse[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].code_name + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].stock_code + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].amount + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + reponse[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + reponse[idx].his_time + "</td>" +
					      "<td class='color-red'>" + reponse[idx].code_name + "</td>" +
					      "<td class='color-red'>" + reponse[idx].stock_code + "</td>" +
					      "<td class='color-red'>" + reponse[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + reponse[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + reponse[idx].amount + "</td>" +
					      "<td class='color-red'>" + reponse[idx].ratio + "</td>" +
					      "<td class='color-red'>" + reponse[idx].profit + "</td>" +
					      "</tr>";
				}
				allDataList.push(str);
			});
			allHistoyTableBody.html(allDataList);
		}, error : function () {
			console.log("실패");
			allHistoyTableBody.html(searchError);
		}
	});
});


$(window).on("load", function () {
	// 현재 날짜 가져오기
	const date = new Date();
	const today = new Intl.DateTimeFormat("kr", {dateStyle : "full"}).format(date);

	$(".historyDate").text(today);

	let errorMsg = "<li>거래된 회사가 없습니다.</li>";
	if (account !== "") {
		$.ajax({
			type     : "POST",
			url      : "/api/data/coList/" + account,
			dataset  : "json",
			success  : function (list) {
				let companyList = [];
				$.each(list, function (idx) {
					str = "<li>" +
					      "<button type='button' class='btn' data-stock-code='" + list[idx].stock_code + "' data-bs-toggle='modal' data-bs-target='#histoyModal'>" +
					      list[idx].code_name +
					      "</button>" +
					      "</li>";
					companyList.push(str);
				});
				coList.html(companyList);
				if (companyList.length === 0) {
					coList.html(errorMsg);
				}
			}, error : function () {
				coList.html(errorMsg);
			}
		});
	}
});
$(document).on("click", ".history-list button", function () {
	let url = "/api/data/coListSearch/" + account + "/" + $(this).data("stock-code");

	let stockCode = $(this).data("stock-code");
	let stockName = $(this).text();

	$("#stockCode").text(stockCode);
	$("#stockName").text(stockName);

	$.ajax({
		type     : "POST",
		url      : url,
		dataset  : "JSON",
		success  : function (history) {
			let historyList = [];
			$.each(history, function (idx) {
				if (parseInt(history[idx].profit) < 0) {
					str = "<tr>" +
					      "<td class='color-blue'>" + history[idx].his_time + "</td>" +
					      "<td class='color-blue'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-blue'>" + history[idx].amount + "</td>" +
					      "<td class='color-blue'>" + history[idx].ratio + "</td>" +
					      "<td class='color-blue'>" + history[idx].profit + "</td>" +
					      "</tr>";
				} else {
					str = "<tr>" +
					      "<td class='color-red'>" + history[idx].his_time + "</td>" +
					      "<td class='color-red'>" + history[idx].sell_num + "</td>" +
					      "<td class='color-red'>" + history[idx].buy_num + "</td>" +
					      "<td class='color-red'>" + history[idx].amount + "</td>" +
					      "<td class='color-red'>" + history[idx].ratio + "</td>" +
					      "<td class='color-red'>" + history[idx].profit + "</td>" +
					      "</tr>";
				}
				historyList.push(str);
			});
			histoyTableBody.html(historyList);
			if (historyList.length === 0) {
				histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
			}
		}, error : function () {
			histoyTableBody.html("<tr><td colspan='6'>거래 내역이 없습니다.</td></tr>");
		}
	});
});

