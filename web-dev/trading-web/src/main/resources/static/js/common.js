const headerMenuBtn = document.querySelector(".header-menu-btn");
const headerMenuList = document.querySelector(".header-menu-list");
const headerMenuListEl = document.querySelectorAll(".header-menu-list li a");
const notLink = document.querySelectorAll("a[href='#']");

const upSort = document.querySelector(".sort-btn");


// 가상 링크 이벤트 최기화
function EventReset(event) {
	event.preventDefault();
}

// 메뉴 딜레이 제거
function menuDelayReset() {
	for (i = 0; i < headerMenuListEl.length; i++) {
		headerMenuListEl[i].style.transitionDelay = ``;
	}
}

// 테블릿, 모바일, 메뉴 버튼 클릭 시 애니메이션
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

