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
					<div class="wrapper">
                        <div class="title"><h1 style="font-size: 21px;">회원가입</h1></div>
                        <div class="user_id">
                            <input id="id"  type="text" placeholder="아이디를 입력해 주세요.">
                            <div id="idError" class="error"></div>
                        </div>
                        <div class="user_pw">
                            <input id="password" type="password" placeholder="비밀번호를 입력해 주세요.">
                            <div id="passwordError" class="error"></div>
                        </div>
                        <div class="user_name">
                            <input id="name" type="text" placeholder="이름을 입력해 주세요.">
                            <div id="nameError" class="error"></div>
                        </div>
                        <div class="user_account">
                            <input id="account" type="password" placeholder="계좌번호를 입력해 주세요.">
                            <div id="accountError" class="error"></div>
                        </div>                        
                        <div class="line">
                            <hr>
                        </div>
                        <div class="signUp">
                            <button id="signUpButton" disabled onclick="signUpCheck()">가입하기</button>
                        </div>
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