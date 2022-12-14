<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩 | 로그인</title>
	<%@ include file="/WEB-INF/views/trading/inc/defualt_css.jsp" %>
	<link rel="stylesheet" href="/css/login.css">
	<c:if test="${loginCheckedMsg != null}">
		<script>
			msg = "${loginCheckedMsg}";
			alert(msg);
			location.href = "/"
		</script>
	</c:if>
</head>
<body>
	<div class="background-wrap">
		<%@ include file="/WEB-INF/views/trading/inc/header.jsp" %>
		<main class="px-4 py-4">
			<section>
				<div class="login-area">
					<h3>로그인</h3>
					<form action="#">
						<ul class="login-input">
							<li>
								<label for="user_id">ID</label>
								<div class="input-bar-style">
									<input type="text" id="user_id" name="user_id" placeholder="아이디를 입력하세요." autocomplete="false"/>
									<div class="input-bar"></div>
								</div>
							</li>
							<li>
								<label for="user_pw">PW</label>
								<div class="input-bar-style">
									<input type="password" id="user_pw" name="user_pw" placeholder="비밀번호를 입력하세요."/>
									<div class="input-bar"></div>
								</div>
							</li>
							<li class="btn-area">
								<button type="button" class="btn btn-primary" id="login-btn">로그인</button>
								<a href="/join" class="btn btn-warning" id="join-btn">
									회원가입
								</a>
							</li>
						</ul>
					</form>
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
	<script src="/js/login_ajax.js"></script>
</body>
</html>