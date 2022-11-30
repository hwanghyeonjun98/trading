<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css">
	<link rel="stylesheet" href="/css/reset.css">
	<link rel="stylesheet" href="/css/common.css">
	<link rel="stylesheet" href="/css/error_common.css">
	<title>트레이딩 | 브라우저 안내</title>
	<script>
		const agent = navigator.userAgent.toLowerCase();
		let msg = '<c:out value="${msg}"/>';
		alert(msg);
	</script>
</head>
<body>
	<div class="error_wrap">
		<div class="error_info">
			<h1 class="text-danger">본 홈페이지는 <b>Internet Explorer</b>를<br/>지원하지 않습니다.</h1>
			<p class="h4"><b>아래 브라우저에서 접속이 가능합니다.</b></p>
			<ul class="browser_list">
				<li>
					<a href="https://whale.naver.com/" title="웨일 브라우저 다운로드 페이지 이동">
						<img src="../img/browser_icon/Whale_icon.svg" alt="네이버 웨일 브라우저 아이콘">
						<h3>웨일</h3>
						<span class="btn btn-primary">다운로드 &nbsp; <i class="bi bi-download"></i></span>
					</a>
				</li>
				<li>
					<a href="https://www.google.com/intl/ko_kr/chrome/" title="크롬 브라우저 다운로드 페이지 이동">
						<img src="../img/browser_icon/Google_Chrome.png" alt="구글 크롬 브라우저 아이콘">
						<h3>Chrome</h3>
						<span class="btn btn-primary">다운로드 &nbsp; <i class="bi bi-download"></i></span>
					</a>
				</li>
				<li>
					<a href="https://www.microsoft.com/ko-kr/edge/home?form=MA13FJ" title="앳지 브라우저 다운로드 페이지 이동">
						<img src="../img/browser_icon/Microsoft_Edge.png" alt="마이크로소프트 앳지 브라우저 아이콘">
						<h3>Edge</h3>
						<span class="btn btn-primary">다운로드 &nbsp; <i class="bi bi-download"></i></span>
					</a>
				</li>
				<li>
					<a href="https://www.mozilla.org/ko/firefox/new/" title="파이어폭스 브라우저 다운로드 페이지 이동">
						<img src="../img/browser_icon/Fx_Browser.svg" alt="파이어폭스 브라우저 아이콘">
						<h3>FierFox</h3>
						<span class="btn btn-primary">다운로드 &nbsp; <i class="bi bi-download"></i></span>
					</a>
				</li>
			</ul>
		</div>
	</div>
</body>
</html>