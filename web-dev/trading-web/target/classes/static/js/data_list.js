// 메뉴 이름 리스트
const indices = ["캐나다 S&P TSX", "나스닥종합지수", "네덜란드 AEX", "닛케이", "다우존스", "대만 가권", "러셀 2000 지수", "러시아 MOEX Russia",
                 "벨기에 BEL", "브라질 보베스파", "사우디아라비아 Tadawul", "상하이종합", "스웨덴 OMXS", "스위스 SMI", "스페인 IBEX",
                 "영국 FTSE", "유로 스톡스 50", "이탈리아 FTSE MIB", "인도네시아 IDX", "코스닥", "코스피 50", "코스피지수", "터키 BIST",
                 "폴란드 WIG 20", "프랑스 CAC", "항셍", "헝가리 BUX", "호주 S&P ASX", "ATX", "BSE 인도 센섹스 30",
                 "CBOE Volatility Index", "DAX", "Dow Jones Shanghai", "FTSE China A50", "Nifty 50", "PSI", "RTSI 지수",
                 "S&P 500", "S&P BMV IPC", "SET Index", "SZSE Component", "TA 35", "VN 30"];

const conins = ["XRP/KRW Bithumb", "BTC/KRW Bithumb", "ETH/KRW Bithumb"];

const commodities = ["WTI유 선물", "천연가스 선물", "은 선물", "미국 소맥 선물", "금 선물", "구리 선물"];

const ratesBonds = ["독일 1년 채권 수익율", "독일 2년 채권 수익율", "독일 3개월 채권 수익율", "독일 3년 채권 수익율", "독일 4년 채권 수익율", "독일 5년 채권 수익율",
                    "독일 6개월 채권 수익율", "독일 6년 채권 수익율", "독일 7년 채권 수익율", "독일 8년 채권 수익율", "독일 9개월 채권 수익율",
                    "독일 9년 채권 수익율", "독일 10년 채권 수익율", "독일 15년 채권 수익율", "독일 20년 채권 수익율", "독일 25년 채권 수익율", "독일 30년 채권 수익율",
                    "러시아 1년 채권 수익율", "러시아 2년 채권 수익율", "러시아 3년 채권 수익율", "러시아 5년 채권 수익율",
                    "러시아 7년 채권 수익율", "러시아 10년 채권 수익율", "러시아 15년 채권 수익율", "러시아 20년 채권 수익율", "미국 1개월 채권 수익율",
                    "미국 1년 채권 수익율", "미국 2년 채권 수익율", "미국 3개월 채권 수익율", "미국 3년 채권 수익율", "미국 5년 채권 수익율",
                    "미국 6개월 채권 수익율", "미국 7년 채권 수익율", "미국 10년물 국채 금리 채권 수익율", "미국 20년 채권 수익율", "미국 30년 채권 수익율",
                    "스위스 1개월 채권 수익율", "스위스 1년 채권 수익율", "스위스 1주 채권 수익율", "스위스 2개월 채권 수익율", "스위스 2년 채권 수익율",
                    "스위스 3개월 채권 수익율", "스위스 3년 채권 수익율", "스위스 4년 채권 수익율", "스위스 5년 채권 수익율", "스위스 6개월 채권 수익율",
                    "스위스 6년 채권 수익율", "스위스 7년 채권 수익율", "스위스 8년 채권 수익율", "스위스 9년 채권 수익율", "스위스 10년 채권 수익율",
                    "스위스 15년 채권 수익율", "스위스 20년 채권 수익율", "스위스 30년 채권 수익율", "스위스 오버나잇 채권 수익율", "영국 1개월 채권 수익율",
                    "영국 1년 채권 수익율", "영국 2년 채권 수익율", "영국 3개월 채권 수익율", "영국 3년 채권 수익율", "영국 4년 채권 수익율",
                    "영국 5년 채권 수익율", "영국 6개월 채권 수익율", "영국 6년 채권 수익율", "영국 7년 채권 수익율", "영국 8년 채권 수익율", "영국 9년 채권 수익율",
                    "영국 10년 채권 수익율", "영국 12년 채권 수익율", "영국 15년 채권 수익율", "영국 20년 채권 수익율",
                    "영국 25년 채권 수익율", "영국 30년 채권 수익율", "영국 40년 채권 수익율", "영국 50년 채권 수익율", "일본 1개월 채권 수익율", "일본 1년 채권 수익율",
                    "일본 2년 채권 수익율", "일본 3개월 채권 수익율", "일본 3년 채권 수익율", "일본 4년 채권 수익율",
                    "일본 5년 채권 수익율", "일본 6개월 채권 수익율", "일본 6년 채권 수익율", "일본 7년 채권 수익율", "일본 8년 채권 수익율", "일본 9개월 채권 수익율",
                    "일본 9년 채권 수익율", "일본 10년 채권 수익율", "일본 15년 채권 수익율", "일본 20년 채권 수익율",
                    "일본 30년 채권 수익율", "일본 40년 채권 수익율", "중국 1년 채권 수익율", "중국 2년 채권 수익율", "중국 3년 채권 수익율", "중국 5년 채권 수익율",
                    "중국 7년 채권 수익율", "중국 10년 채권 수익율", "중국 15년 채권 수익율", "중국 20년 채권 수익율",
                    "중국 30년 채권 수익율", "터키 2년 채권 수익율", "터키 3개월 채권 수익율", "터키 3년 채권 수익율", "터키 5년 채권 수익율", "터키 6개월 채권 수익율",
                    "터키 9개월 채권 수익율", "터키 10년 채권 수익율", "프랑스 1개월 채권 수익율", "프랑스 1년 채권 수익율",
                    "프랑스 2년 채권 수익율", "프랑스 3개월 채권 수익율", "프랑스 3년 채권 수익율", "프랑스 4년 채권 수익율", "프랑스 5년 채권 수익율",
                    "프랑스 6개월 채권 수익율", "프랑스 6년 채권 수익율", "프랑스 7년 채권 수익율", "프랑스 8년 채권 수익율", "프랑스 9개월 채권 수익율",
                    "프랑스 9년 채권 수익율", "프랑스 10년 채권 수익율", "프랑스 15년 채권 수익율", "프랑스 20년 채권 수익율", "프랑스 25년 채권 수익율",
                    "프랑스 30년 채권 수익율", "프랑스 50년 채권 수익율", "한국 1년 채권 수익율", "한국 2년 채권 수익율", "한국 3년 채권 수익율",
                    "한국 4년 채권 수익율", "한국 5년 채권 수익율", "한국 10년 채권 수익율", "한국 20년 채권 수익율", "한국 30년 채권 수익율", "한국 50년 채권 수익율"];

const currencies = ["AED/KRW", "AUD/KRW", "CAD/KRW", "CHF/KRW", "CNY/KRW", "DKK/KRW", "EUR/KRW", "GBP/KRW", "HKD/KRW",
                    "IDR/KRW", "INR/KRW", "JPY/KRW", "MXN/KRW", "MYR/KRW", "NOK/KRW", "NZD/KRW",
                    "PKR/KRW", "SAR/KRW", "SEK/KRW", "SGD/KRW", "THB/KRW", "USD/KRW"];

// 메뉴 대분류
const currenciesListEl = document.querySelector(".currencies");
const indicesListEl = document.querySelector(".indices");
const commoditiesListEl = document.querySelector(".commodities");
const ratesBondsListEl = document.querySelector(".rates_bonds");
const coninsListEl = document.querySelector(".conins");

// 메뉴 동적으로 생성
function menuList(list, listName) {
	for (i = 0; i < list.length; i++) {
		let tempLi = document.createElement("li");
		let tempA = document.createElement("a");
		let aText = list[i];

		tempA.classList.add("data-view-btn");
		tempA.setAttribute("type", "button");
		if (aText === "독일 3개월 채권 수익율") {
			tempA.setAttribute("href", "/dataview/data/germany3month채권수익율");
			tempA.dataset.table = "germany3month채권수익율";
		} else {
			tempA.setAttribute(
				"href", `/dataview/data/${aText.replaceAll("/", "").replaceAll(" ", "").replaceAll("&", "").toLowerCase()}`);
			tempA.dataset.table = aText.replaceAll("/", "").replaceAll(" ", "").replaceAll("&", "").toLowerCase();
		}
		tempA.innerText = aText;
		tempLi.append(tempA);

		listName.append(tempLi);
	}
}

menuList(currencies, currenciesListEl);
menuList(indices, indicesListEl);
menuList(commodities, commoditiesListEl);
menuList(ratesBonds, ratesBondsListEl);
menuList(conins, coninsListEl);

// 브라우저 로드 시 버튼 활성화, 제목 변경
window.addEventListener("load", () => {
		// 현재 브라우저 URL 불러와 맨뒤 내역 이름 가져오기
		const nowUrl = decodeURI(window.location.href);
		let name = nowUrl.split("/");
		name = name[name.length - 1];

		// 가져온 이름과 dataset 이름으로 비교하여
		// 버튼 활성화하고 데이터 제목 업데이트
		const btnAll = document.querySelectorAll(".data-view-btn");
		const dataTitle = document.querySelector(".data-title .data-name");
		const dataTable = document.querySelector("#data-table");

		if (name === "data") {
			dataTable.dataset.table = "aedkrw";
		} else {
			console.log('다름');
			btnAll.forEach((el) => {
				const dataName = el.dataset.table;

				if (dataName === name) {
					el.classList.add("active");
					dataTitle.innerText = el.textContent;
				}
			});
			dataTable.dataset.table = name;
		}
	}
);

// 대분류 클릭 시 하위 메뉴 토글 슬라이드
const menuTitle = document.querySelectorAll(".menu-title");
const menuContent = document.querySelectorAll(".menu-content");
const menu = document.querySelectorAll(".menu-content ul");
const menuIcon = document.querySelectorAll(".icon-span i");

function menuContentHeight(idx) {
	let menuMarginTop = parseInt(getComputedStyle(menu[idx]).marginTop);
	let menuMarginBottom = parseInt(getComputedStyle(menu[idx]).marginBottom);
	let menuHeight = menu[idx].offsetHeight + menuMarginTop + menuMarginBottom;

	menuContent[idx].style.maxHeight = `${menuHeight}px`;
}

menuTitle.forEach((el, idx) => {
	el.addEventListener("click", (event) => {
		if (!event.currentTarget.classList.contains("active")) {
			event.currentTarget.classList.add("active");
			menuContentHeight(idx);
			menuIcon[idx].className = "bi bi-arrow-bar-up";
		} else {
			event.currentTarget.classList.remove("active");
			menuContent[idx].style.maxHeight = `0`;
			menuIcon[idx].className = "bi bi-arrow-bar-down";
		}
	});
});

// 메뉴 클릭 시 강조
const menuBtn = document.querySelectorAll(".data-view-btn");
const dataTitle = document.querySelector(".data-name");

menuBtn.forEach((btn) => {
	btn.addEventListener("click", (event) => {
		for (i = 0; i < menuBtn.length; i++) {
			menuBtn[i].classList.remove("active");
		}
		event.currentTarget.classList.add("active");

		dataTitle.innerText = btn.textContent;
	});
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
console.log(dateCalc);

// 현재 날짜
endDateInput.value = nowDate;
// 검색 최대 날짜 정해기
endDateInput.setAttribute("max", nowDate);