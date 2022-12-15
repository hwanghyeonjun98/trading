const historyBackBtn = document.querySelector(".page-back");

// 에러 페이지에서 뒤로가기 버튼 클릭 시 이전페이지로 이동
historyBackBtn.addEventListener("click", () => {
	history.back();
});