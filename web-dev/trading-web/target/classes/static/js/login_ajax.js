function login() {
	const userId = $("#user_id").val();
	const userPw = $("#user_pw").val();
	if (userId === "" || userPw === "") {
		// event.preventDefault();
		alert("로그인 정보를 입력하세요.");

		$("#user_id").focus();
	} else {
		$.ajax({
			type       : "POST",
			url        : "/login/userLogin",
			data       : "user_id=" + userId + "&user_pw=" + userPw,
			dataset    : "text",
			success    : function (data) {
				if (data === "true") {
					location.href = "/";
				} else {
					// event.preventDefault();
					alert("로그인 정보를 확인하세요.");
				}
			},
			error      : function () {
				alert("로그인 정보가 잘못 되었습니다.\n문제가 계속되면 관리자에게 연락주세요.");
			}, timeout : 10000
		});
	}
}

function loginButtonKeyPress(event) {
	if (event.keyCode === 13) {
		login();
	}
}

$("input").on("change", function () {
	if ($(this).val() !== "") {
		$(this).addClass("active");
	} else {
		$(this).removeClass("active");
	}
});

$("#login-btn").on("click", event => login(event));
$(window).on("keyup", event => loginButtonKeyPress(event));