<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩 | 404</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css">
	<link rel="stylesheet" href="/css/reset.css">
	<link rel="stylesheet" href="/css/common.css">
	<link rel="stylesheet" href="/css/error_common.css">
	<script src="https://kit.fontawesome.com/5787bde1c1.js" crossorigin="anonymous"></script>
</head>
<body>
	<div class="error_wrap">
		<div class="error_info">
			<h1 class="error_code">404</h1>
			<h2 class="error_text"><i class="bi bi-info-circle"></i> 없는 페이지 입니다.</h2>
			<p>
				홈페이지 경로가 잘못되었거나, 페이지가 없습니다. <br>
				홈페이지 주소를 확인해 주세요!
			</p>
			<ul class="error_btn">
				<li>
					<a href="#" class="page-back btn btn-outline-secondary btn-lg">이전으로 돌아가기 <i class="bi bi-arrow-counterclockwise"></i></a>
				</li>
				<li>
					<a href="/" class="btn btn-outline-primary btn-lg">메인 페이지 <i class="bi bi-house"></i></a>
				</li>
			</ul>
		</div>
	</div>
	<script src="/js/error_page.js"></script>
</body>
</html>