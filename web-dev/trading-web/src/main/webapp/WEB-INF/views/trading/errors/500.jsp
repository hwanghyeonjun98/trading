<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩 | 500</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css">
	<link rel="stylesheet" href="/css/reset.css">
	<link rel="stylesheet" href="/css/common.css">
	<link rel="stylesheet" href="/css/error_common.css">
</head>
<body>
	<div class="error_wrap">
		<div class="error_info">
			<h1 class="error_code opacity-50">500</h1>
			<h2 class="error_text"><i class="bi bi-info-circle"></i> 잘못된 접근입니다.</h2>
			<ul class="error_btn">
				<li>
					<a href="#" class="page-back btn btn-outline-secondary btn-lg">이전으로 돌아가기
						<i class="bi bi-arrow-counterclockwise"></i></a>
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