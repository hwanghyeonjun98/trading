const headerMenuBtn = document.querySelector(".header-menu-btn"); // 모바일 화면 오른쪽 상단 버튼
const headerMenuList = document.querySelector(".header-menu-list"); // 모바일 화면 사이드 매뉴
const headerMenuListEl = document.querySelectorAll(".header-menu-list li a"); // 모바일 화면 사이드 메뉴 요소들
const notLink = document.querySelectorAll("a[href='#']"); // 가상링크로 되어있는 a태그들
const topBtn = document.querySelector(".top-to-btn"); // 상단으로 올라가는 버튼
const logoutBtn = document.querySelector(".logout-btn"); // 로그아웃 버튼

// 가상 링크 이벤트 초기화(작동안되게)
function EventReset(event) {
	event.preventDefault();
}

// 메뉴 딜레이 제거
function menuDelayReset() {
	for (i = 0; i < headerMenuListEl.length; i++) {
		headerMenuListEl[i].style.transitionDelay = ``;
	}
}

// 테블릿, 모바일 화면에서 메뉴 버튼 클릭 시 애니메이션
function mobileMenuClick() {
	if (window.outerWidth < `1024`) {
		headerMenuList.classList.toggle("active");
		delay = .25;
		for (i = 0; i < headerMenuListEl.length; i++) {
			delay += .25;
			headerMenuListEl[i].style.transitionDelay = `${delay}s`;
		}

		setTimeout(menuDelayReset, 500);
	}
}

// 메뉴 버튼 영역 외 클릭 시 메뉴 닫히게하기
function otherSpaceClick(event) {
	target = event.target;
	if (!headerMenuBtn.contains(target)) {
		headerMenuList.classList.remove("active");
	}
}

// 가상 링크 클릭 이벤트 리스너
notLink.forEach((a) => {
	a.addEventListener("click", EventReset);
});

// 메뉴 관련 이벤트 리스너
headerMenuBtn.addEventListener("click", mobileMenuClick);
document.addEventListener("click", otherSpaceClick);

// 오른쪽 하단 버튼 클릭 시 상단으로 이동
topBtn.addEventListener("click", () => {
	window.scrollTo(0, 0);
});

// 일정 수치 만큼 스크롤 시 버튼 표시
window.addEventListener("scroll", () => {
	let scrollTop = window.scrollY;
	if (scrollTop > 500) {
		topBtn.classList.add("active");
	} else {
		topBtn.classList.remove("active");
	}
});

// 로그아웃 버튼 존재시 적용
if (logoutBtn !== null) {
	// 로그아웃 이벤트
	function logoutClick() {
		const logpoutConfrim = confirm("로그아웃 하시겠습니까?");
		if (logpoutConfrim === true) {
			location.href = "/logout";
		}

		if (logpoutConfrim === false) {
			return false;
		}
	}

	logoutBtn.addEventListener("click", logoutClick);
}

var tooltipTriggerList = [].slice.call(document.querySelectorAll("[data-bs-toggle=\"tooltip\"]"));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
	return new bootstrap.Tooltip(tooltipTriggerEl);
});

// 날짜 관련
const startDateInput = document.querySelector("#startDate");
const endDateInput = document.querySelector("#endDate");
let date = new Date(); // 날짜 object 생성
const TIME_ZONE = 3240 * 10000; // 한국 시간대로 타임존 setting
const nowDate = new Date(+date + TIME_ZONE).toISOString().split("T")[0]; // 한국 시간으로 불러와 T를 기준으로 split

// 한달전 날짜
date.setMonth(date.getMonth() - 1);
const dateCalc = date.toISOString().split("T")[0];

startDateInput.value = dateCalc;

// 현재 날짜
endDateInput.value = nowDate;

// 검색 최대 날짜
startDateInput.setAttribute("max", nowDate);
endDateInput.setAttribute("max", nowDate);

if (startDateInput.getAttribute("type") === "datetime-local"
    && endDateInput.getAttribute("type") === "datetime-local") {
	startDateInput.value = dateCalc + "T00:00";
	endDateInput.value = nowDate + "T23:59";

	startDateInput.setAttribute("max", nowDate + "T23:59");
	endDateInput.setAttribute("max", nowDate + "T23:59");
}
