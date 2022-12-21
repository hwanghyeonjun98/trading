var rolling = document.getElementById("rolling");

window.setInterval(function () {

	rolling.style.transitionDuration = "400ms";
	rolling.style.marginTop = "-2em";

	window.setTimeout(function () {

		rolling.removeAttribute("style");
		rolling.appendChild(rolling.firstElementChild);

	}, 400);
}, 2000);

const defaultDate = new Date();
document.querySelector("#current").innerHTML = defaultDate.toLocaleTimeString();

setInterval(displayNow, 1000); // 1초마다 시간 갱신
function displayNow() {
	const now = new Date();
	//현재 거주 지역에 맞는 시간
	document.querySelector("#current").innerHTML = now.toLocaleTimeString();
}

