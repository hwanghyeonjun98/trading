<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css">
	<link rel="stylesheet" href="/css/reset.css">
	<link rel="stylesheet" href="/css/common.css">
	<script src="/js/browserCheck.js"></script>
	<script src="https://kit.fontawesome.com/5787bde1c1.js" crossorigin="anonymous"></script>
</head>
<body>
	<div class="background-wrap">
		<header class="p-3">
			<h1 class="h2"><a href="/">단타 주식 가격 예측</a></h1>
			<nav>
				<div class="mobile-show">
					<button type="button" class="header-menu-btn">
						<i class="bi bi-list"></i>
					</button>
				</div>
				<ul class="header-menu-list">
					<li><a href="#">홈</a></li>
					<li><a href="#">데이터 보기</a></li>
					<li><a href="#">연락처</a></li>
				</ul>
			</nav>
		</header>
		<main class="p-3">
			<section>
				<article>
					<h2 class="h4">내용 들어 갈 자리</h2>
					<div id="chart-area">
					</div>
				</article>
			</section>
		</main>
		<footer class="p-3">
			<div class="info">
				<p class="">책임 없음</p>
			</div>
			<div class="copyright">
				<p>빅데이터 15기 주가예측팀</p>
				<p>권준섭, 김민건, 김성진, 김영운, 윤성한, 황현준</p>
			</div>
		</footer>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="/js/common.js"></script>
</body>
</html>