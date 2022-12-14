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
	<link rel="stylesheet" href="/css/index.css">
	
	
</head>
<body>
	<div class="background-wrap">
		<%@ include file="/WEB-INF/views/trading/inc/header.jsp" %>
			<main class="p-3">
			<p>TIME : <span id="current" class="display"></span></p>
			<script>
				setInterval(displayNow, 1000); // 1초마다 시간 갱신
				function displayNow() {
				let now = new Date();
				let currentTime = now.toLocaleTimeString();//현재 거주 지역에 맞는 시간

				document.querySelector("#current").innerHTML = currentTime
				}

			</script>
			<section>
				<article>
						<div class="clear-wrapper">
						</div>
					<div class="recommendation-keywords-container">
						<div class="titlecu"><h2>환율 검색 추천</h2></div>
						<div class="keywords-container-wrapper">
							<div class="keywords-contents">
								<a href="/dataview/data/cadkrw">
									<div class="keyword item">CAD/KRW</div>
								</a>
								<a href="/dataview/data/chfkrw">
									<div class="keyword item">CHF/KRW</div>
								</a>
								<a href="/dataview/data/cnykrw">
									<div class="keyword item">CNY/KRW</div>
								</a>
								<a href="/dataview/data/dkkkrw">
									<div class="keyword item">DKK/KRW</div>
								</a>
								<a href="/dataview/data/eurkrw">
									<div class="keyword item">EUR/KRW</div>
								</a>
								<a href="/dataview/data/gbpkrw">
									<div class="keyword item">GBP/KRWS</div>
								</a>
								<a href="/dataview/data/hkdkrw">
									<div class="keyword item">HKD/KRW</div>
								</a>
								<a href="/dataview/data/idrkrw">
									<div class="keyword item">IDR/KRW</div>
								</a>
								<a href="/dataview/data/jpykrw">
									<div class="keyword item">JPY/KRW</div>
								</a>
								<a href="/dataview/data/sgdkrw">
									<div class="keyword item">SGD/KRW</div>
								</a>
								<a href="/dataview/data/thbkrw">
									<div class="keyword item">THB/KRW</div>
								</a>
								<a href="/dataview/data/usdkrw">
									<div class="keyword item">USD/KRW</div>
								</a>
							</div>
						</div>
						<div class="titlecu"><h2>세계지수 검색 추천</h2></div>
						<div class="keywords-container-wrapper">
							<div class="keywords-contents">
								<a href="/dataview/data/캐나다sptsx">
									<div class="keyword item">캐나다 S&P TSX</div>
								</a>
								<a href="/dataview/data/나스닥종합지수">
									<div class="keyword item">나스닥종합지수</div>
								</a>
								<a href="/dataview/data/네덜란드aex">
									<div class="keyword item">네덜란드 AEX</div>
								</a>
								<a href="/dataview/data/닛케이">
									<div class="keyword item">닛케이</div>
								</a>
								<a href="/dataview/data/다우존스">
									<div class="keyword item">다우존스</div>
								</a>
								<a href="/dataview/data/대만가권">
									<div class="keyword item">대만 가권</div>
								</a>
								<a href="/dataview/data/러셀2000지수">
									<div class="keyword item">러셀 2000 지수</div>
								</a>
								<a href="/dataview/data/러시아moexrussia">
									<div class="keyword item">러시아 MOEX Russia</div>
								</a>
								<a href="/dataview/data/벨기에bel">
									<div class="keyword item">벨기에 BEL</div>
								</a>
								<a href="/dataview/data/브라질보베스파">
									<div class="keyword item">브라질 보베스파</div>
								</a>
								<a href="/dataview/data/사우디아라비아tadawul">
									<div class="keyword item">사우디아라비아 Tadawul</div>
								</a>
							</div>
						</div>
					</div>
					<a href="https://deepsearch-jira.atlassian.net/servicedesk/customer/kb/view/636583937" class="banner" target="_blank" rel="noopener noreferrer">
						<img src="https://deepsearchimages.wpcomstaging.com/wp-content/uploads/cards/2022/11/banner_20221124-20221124-053132.png" alt="[DAP] 경제 지표 개선 공지">
					</a>
					<h2 class="main_title">이 시각 주요 뉴스</h2>
					<div class="groups">
						<div class="economic-indicator">
							<div class="jot"></div>
							<div id="root">
							</div>
							<script src='app.js' type="module"></script>
							<div class="indicator-name">
								<a href="/analytics/economic-indicator/BOK%3A802Y001.0001000">코스피</a>
							</div>
							<div class="main-value"><span class="change-rate_neg">2,419.32</span>
							</div>
							<div class="sub-value">3일 전 대비<span class="change-rate_neg">-0.62%</span></div>
							<div class="sub-value">전년도 대비<span class="change-rate_neg">-18.5%</span></div>
							<div class="date-info">
								<div class="cycle">주기: Daily</div>
								<div class="date">2022. 12. 05</div>
							</div>
						</div>
						<div class="economic-indicator">
							<div class="indicator-name">
								<a href="/analytics/economic-indicator/BOK%3A802Y001.0089000">코스닥</a>
							</div>
							<div class="main-value"><span class="change-rate_pos">733.32</span>
							</div>
							<div class="sub-value">3일 전 대비<span class="change-rate_pos">+0.05%</span></div>
							<div class="sub-value">전년도 대비<span class="change-rate_neg">-26.56%</span></div>
							<div class="date-info">
								<div class="cycle">주기: Daily</div>
								<div class="date">2022. 12. 05</div>
							</div>
						</div>
						<div class="economic-indicator">
							<div class="indicator-name">
								<a href="/analytics/economic-indicator/BOK%3A731Y001.0000001">원달러환율</a>
							</div>
							<div class="main-value"><span class="change-rate_neg">1,293.2</span></div>
							<div class="sub-value">전월대비<span class="change-rate_neg">-9.06%</span></div>
							<div class="sub-value">전년도 대비<span class="change-rate_pos">+9.72%</span></div>
							<div class="date-info">
								<div class="cycle">주기: Daily</div>
								<div class="date">2022. 12. 06</div>
							</div>
						</div>
						<div class="economic-indicator">
							<div class="indicator-name">
								<a href="/analytics/economic-indicator/BOK%3A817Y002.010101000">콜금리</a>
							</div>
							<div class="main-value"><span class="change-rate_pos">3.224</span></div>
							<div class="sub-value">전월대비<span class="change-rate_pos">+7.75%</span></div>
							<div class="sub-value">전년도 대비<span class="change-rate_pos">+237.59%</span></div>
							<div class="date-info">
								<div class="cycle">주기: Daily</div>
								<div class="date">2022. 12. 05</div>
							</div>
						</div>
					</div>

					<div class="chartFrame">
						<h2>코스피 지수 현황</h2>
									<div id="chart-area">
									</div>			
									<h2>시가 총액 상위</h2>
										<hr />
										   <div id="container">
											<ul id="rolling">
												<li>1.삼성전자</li>
												<li>2.LG 에너지 솔루션</li>
												<li>3.SK하이닉스</li>
												<li>4.삼성바이오로직스</li>
												<li>5.삼성SDI</li>
												<li>6.LG화학</li>
												<li>7.삼성전자우</li>
												<li>8.현대차</li>
												<li>9.NAVER</li>
												<li>10.카카오</li>
											</ul>
											</div>
													
					</div>	

					<div id="chart-area">
						
					</div>
				</article>
			</section>

		</main>
		<%@ include file="/WEB-INF/views/trading/inc/footer.jsp" %>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>	
	<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
	<script src="/js/common.js"></script>
	<script src="/js/index_chart.js"></script>
	<script src="/js/index_ajax.js"></script>
</body>
</html>