<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩 | 개발자 소개</title>
	<%-- 기본적으로 불러와야 하는 것--%>
	<%@ include file="/WEB-INF/views/trading/inc/defualt_css.jsp" %>
	<link rel="stylesheet" href="/css/developer_info.css">
</head>
<body>
	<div class="background-wrap">
		<%-- haeder include--%>
		<%@ include file="/WEB-INF/views/trading/inc/header.jsp" %>
		<%-- haeder include--%>
		<main class="p-3 sub-page">
			<section>
				<h4 class="h6 mb-1">더조은컴퓨터아카데믹 빅데이터 분석&추천시스템 개발자 양성과정</h4>
				<h3 class="h1">주식 종목 빅데이터 AI 예측팀</h3>
				<article>
					<h3>팀장</h3>
					<div class="team">
						<ul>
							<li>황현준</li>
							<li>역할 : 데이터 수집, 프론트엔드/백엔드</li>
						</ul>
					</div>
					<h3>팀원</h3>
					<div class="team">
						<ul>
							<li>김성진</li>
							<li>역할 : 데이터 수집, 프론트엔드/백엔드</li>
						</ul>
						<ul>
							<li>김민건</li>
							<li>역할 : 데이터 수집, ML(머신러링)</li>
						</ul>
						<ul>
							<li>김영운</li>
							<li>역할 : 데이터 수집, ML(머신러링))</li>
						</ul>
						<ul>
							<li>권준섭</li>
							<li>역할 : 데이터 수집, RL(강화학습)</li>
						</ul>
						<ul>
							<li>윤성환</li>
							<li>역할 : 데이터 수집, RL(강화학습)</li>
						</ul>
					</div>
				</article>
				<article>
					<h3>프로젝트 기간</h3>
					<p class="ps-3">2022년 10월 12일 ~ 2023년 01월 13일</p>
				</article>
				<article>
					<h3>사용 기술(언어)</h3>
					<h4 class="h5 ps-3">ML, DL, RL</h4>
					<ul class="skill-list ps-3">
						<li>
							<div class="img-warp"><img src="../img/skill_icon/python.svg" alt="Python" class="skill-img"></div>
							Python
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/tensorflow.svg" alt="tensorflow" class="skill-img">
							</div>
							tensorflow
						</li>
					</ul>
					<h4 class="h5 ps-3">frontend</h4>
					<ul class="skill-list">
						<li>
							<div class="img-warp"><img src="../img/skill_icon/html.png" alt="HTML" class="skill-img"></div>
							HTML
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/css.png" alt="CSS3" class="skill-img"></div>
							CSS3
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/bs.png" alt="BOOTSTRAP" class="skill-img"></div>
							BOOTSTRAP
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/js.png" alt="JAVASCRPIT" class="skill-img"></div>
							JAVASCRPIT (ES6+)
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/jq.png" alt="JQUERY" class="skill-img"></div>
							JQUERY (ajax 부분)
						</li>
					</ul>
					<h4 class="h5 ps-3">backend</h4>
					<ul class="skill-list">
						<li>
							<div class="img-warp"><img src="../img/skill_icon/java.png" alt="JAVA" class="skill-img"></div>
							JAVA
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/java.png" alt="jsp" class="skill-img"></div>
							jsp
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/spring.svg" alt="spring" class="skill-img"></div>
							spring boot
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/mysql.png" alt="MY SQL" class="skill-img"></div>
							MY SQL
						</li>
						<li>
							<div class="img-warp"><img src="../img/skill_icon/mybatis.svg" alt="mybatis" class="skill-img"></div>
							mybatis
						</li>
					</ul>
				</article>
				<article>
					<h3>데이터 출처</h3>
					<ul>
						<li>investing
							<ul>
								<li>환율/채권/원자재/세계지수/암호회폐</li>
							</ul>
						</li>
						<li>금융감독원 전자공시 시스템 DART
							<ul>
								<li>국내 기업 재무제표</li>
							</ul>
						</li>
						<li>대신증권
							<ul>
								<li>대싡증권 API 크래온</li>
								<li>국내 기업 주식 정보</li>
							</ul>
						</li>
						<li>KRX 정보데이터시스템
							<ul>
								<li>시가총액 순위</li>
								<li>국내 상장 기업 리스트</li>
							</ul>
						</li>
					</ul>
				</article>
			</section>
		</main>
		<%-- footer include--%>
		<%@ include file="/WEB-INF/views/trading/inc/footer.jsp" %>
		<%-- footer include--%>
	</div>
	<button type="button" class="top-to-btn">
		<i class="bi bi-arrow-up-circle-fill"></i>
	</button>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="/js/common.js"></script>
</body>
</html>