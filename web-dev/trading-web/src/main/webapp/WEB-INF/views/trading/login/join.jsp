<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩</title>
	<%@ include file="/WEB-INF/views/trading/inc/defualt_css.jsp" %>
	<link rel="stylesheet" href="/css/login.css">
</head>
<body>
	<div class="background-wrap">
		<%@ include file="/WEB-INF/views/trading/inc/header.jsp" %>
		<main class="px-4 py-4">
			<section>
				<div class="join-area">
					<h3>회원가입</h3>
					<ul class="join-input">
						<li>
							<label for="user_id">아이디 *</label>
							<div class="input-bar-style me-3">
								<input id="user_id" name="user_id" type="text" placeholder="아이디를 입력해 주세요." required>
								<div class="input-bar"></div>
							</div>
							<button id="idCheckBtn" type="button" class="btn btn-sm">중복확인</button>
						</li>
						<li class="id-check-li">
							<p>중복 되는 아이디가 있습니다.</p>
						</li>
						<li>
							<label for="user_pw">비밀번호 *</label>
							<div class="input-bar-style">
								<input id="user_pw" name="user_pw" type="password" placeholder="비밀번호를 입력해 주세요." required>
								<div class="input-bar"></div>
							</div>
						</li>
						<li>
							<label for="pw_check">비밀번호 <br>확인 *</label>
							<div class="input-bar-style">
								<input id="pw_check" type="password" placeholder="비밀번호를 입력해 주세요." required>
								<div class="input-bar"></div>
							</div>
						</li>
						<li class="pw-check-li">
							<p>비밀번호가 다릅니다. 비밀번호를 확인해주세요.</p>
						</li>
						<li>
							<label for="user_id">이름 *</label>
							<div class="input-bar-style">
								<input id="user_name" name="user_name" type="text" placeholder="이름을 입력해 주세요." required>
								<div class="input-bar"></div>
							</div>
						</li>
						<li>
							<label for="user_id">계좌번호 *</label>
							<div class="input-bar-style">
								<input id="user_account" name="user_account" type="text" placeholder="계좌번호를 입력해 주세요." required>
								<div class="input-bar"></div>
							</div>
						</li>
						<li>
							<button id="signUpButton" type="button">가입하기</button>
						</li>
					</ul>
					<form></form>
				</div>
			</section>
		</main>
		<%@ include file="/WEB-INF/views/trading/inc/footer.jsp" %>
	</div>
	<button type="button" class="top-to-btn">
		<i class="bi bi-arrow-up-circle-fill"></i>
	</button>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
	<script src="/js/common.js"></script>
	<script src="/js/join.js"></script>
</body>
</html>