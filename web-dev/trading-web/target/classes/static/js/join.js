const idCheckbtn = $("#idCheckBtn");
const idInput = $("#user_id");
const signUpBtn = $("#signUpButton");
let idCheck = false;

// 아이디 중복 확인
idCheckbtn.on("click", function () {
	if (idInput.val() === "") {
		$(".id-check-li").text("아이디를 입력하세요,");
		$(".id-check-li").addClass("active");
		return idCheck = false;
	}
	$.ajax({
		type    : "POST",
		url     : "/join/idCheck/" + idInput.val(),
		dataset : "json",
		success : function (data) {
			if (data === "hadId") {
				$(".id-check-li").text("중복되는 아이디가 있습니다.");
				$(".id-check-li").addClass("active");

				return idCheck = false;
			} else {
				$(".id-check-li").text("사용 가능한 아이디입니다.");
				$(".id-check-li").addClass("active");
				return idCheck = true;
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