(function ranking() {
	$.ajax({
		type       : "POST",
		url        : "/api/data/marketCapRanking",
		dataset    : "json",
		success    : function (ranking) {
			const list = [];
			$.each(ranking, function (index) {
				str = "<li>" + ranking[index].no + ". " + ranking[index].stock_name + "</li>";
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
	//현재 거주 지역에 맞는 시간
	document.querySelector("#current").innerHTML = now.toLocaleTimeString();
}

