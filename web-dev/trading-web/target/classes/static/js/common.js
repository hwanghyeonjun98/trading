const headerMenuBtn = document.querySelector(".header-menu-btn"); // 모바일 화면 오른쪽 상단 버튼
const headerMenuList = document.querySelector(".header-menu-list"); // 모바일 화면 사이드 매뉴
const headerMenuListEl = document.querySelectorAll(".header-menu-list li a"); // 모바일 화면 사이드 메뉴 요소들
const notLink = document.querySelectorAll("a[href='#']"); // 가상링크로 되어있는 a태그들

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

