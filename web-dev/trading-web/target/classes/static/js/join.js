const idCheckbtn = $("#idCheckBtn");
const idInput = $("#user_id");
const signUpBtn = $("#signUpButton");

// 아이디 중복 확인
idCheckbtn.on("click", function (event) {
	if (idInput.val() === "") {
		event.preventDefault();
		$(".id-check-li").text("아이디를 입력하세요,");
	}
	$.ajax({
		type    : "POST",
		url     : "/join/idCheck/" + idInput.val(),
		dataset : "json",
		success : function (data) {
			if (data === "hadId") {
				$(".id-check-li").text("중복되는 아이디가 있습니다.");
				$(".id-check-li").addClass("active");
			} else {
				$(".id-check-li").removeClass("active");
			}
		}
	});
});

// 비밇번호 체크
$("input[id*=pw]").on("change", function () {
	if ($("#user_pw").val() !== $("#pw_check").val()) {
		$(".pw-check-li").addClass("active");
	} else {
		$(".pw-check-li").removeClass("active");
	}
});

// 가입하기