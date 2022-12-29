const idCheckbtn = $("#idCheckBtn");
const idInput = $("#user_id");
const pwInput = $("#user_pw");
const idCheckLi = $(".id-check-li");
const pwCheckLi = $(".pw-check-li");
let idCheck = false;
let pwCheck = false;

const bsesstion = window.sessionStorage;

// 아이디 정규식
const idRegx = /^[a-zA-Z\d]+$/;
const pwRegx = /^[a-zA-Z\d@$!%*#?&]+$/;


// 아이디 중복 확인
idCheckbtn.on("click", function () {
	if (idInput.val() === "") {
		idCheckLi.text("아이디를 입력하세요.");
		idCheckLi.addClass("active");
		return idCheck = false;
	}

	if (!idRegx.test(idInput.val())) {
		idCheckLi.text("아이디를 영어로 입력해주세요");
		idCheckLi.addClass("active");

		return idCheck = false;
	}

	$.ajax({
		type    : "POST",
		url     : "/join/idCheck/" + idInput.val(),
		dataset : "json",
		success : function (data) {
			if (data === "hadId") {
				idCheckLi.text("중복되는 아이디가 있습니다.");
				idCheckLi.addClass("active");

				return idCheck = false;
			} else {
				idCheckLi.text("사용 가능한 아이디입니다.");
				idCheckLi.addClass("active");
				return idCheck = true;
			}
		}
	});
});

// 비밀번호 체크
$("input[id*=pw]").on("change", function () {
	if (pwInput.val() !== $("#pw_check").val() || !pwRegx.test(pwInput.val())) {
		pwCheckLi.addClass("active");
		pwCheck = false;
	} else {
		pwCheckLi.removeClass("active");
		pwCheck = true;
	}
});

// 가입하기
$("#userJoin").on("submit", function (event) {
	if (idInput === false) {
		event.preventDefault();
		alert("아이디가 중복 되거나 형식이 일치 하지 않습니다.");
		idInput.focus();
	}

	if (pwCheck === false) {
		event.preventDefault();
		alert("비밀번호 형식이 맞지 않거나 비밀번호가 다릅니다.");
		pwInput.focus();
	}

	if (idCheck === true && pwCheck === true) {
		alert("축하합니다. 회원가입이 완료되었습니다!\n로그인 페이지에서 로그인해주세요!");
		bsesstion.setItem("joinCheck", "true");
	} else {
		event.preventDefault();
		alert("로그인 정보를 정확히 입력해주세요.");
	}
});