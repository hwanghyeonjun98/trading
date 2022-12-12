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
			<section>
				<article>
					<div class="search-bar-content">
						<div class="clear-wrapper">
						</div>
					</div>
					<div class="recommendation-keywords-container">
						<div class="titlecu"><h2>환율 검색 추천</h2></div>
						<div class="keywords-container-wrapper">
							<div class="keywords-contents">
								<a href="/dataview/data/caddkrw">
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

					<h2 class="main_title">국내 금융시장 주요 지표</h2>
					<div class="groups">
						<div class="economic-indicator">
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
						
						<div id="chart-area">
						
						</div>
						
				
									
													<div class="aside_area aside_popular"> 
														<h3 class="h_popular"><span>인기 검색 종목</span></h3> 
														<table class="tbl_home">
														 <colgroup> 
														  <col> 
														  <col width="60"> 
														  <col width="82"> 
														 </colgroup> 
														 <thead> 
														  <tr> 
														   <th scope="col">구분</th> 
														   <th scope="col">현재가</th> 
														   <th scope="col">전일대비</th> 
														  </tr> 
														 </thead> 
														 <tbody> 
														  <tr class="up"><th scope="row"><em>1.</em><a href="/item/main.naver?code=005930" onclick="clickcr(this, &quot;boa.list&quot;, &quot;005930&quot;, &quot;1&quot;, event);">삼성전자</a></th><td>59,000</td><td><em class="bu_p bu_pup"><span class="blind">상승</span></em><span class="tah p11 red02"> 100 </span></td></tr> 
														  <tr class="down"><th scope="row"><em>2.</em><a href="/item/main.naver?code=112040" onclick="clickcr(this, &quot;boa.list&quot;, &quot;112040&quot;, &quot;2&quot;, event);">위메이드</a></th><td>29,900</td><td><em class="bu_p bu_pdn"><span class="blind">하락</span></em><span class="tah p11 nv01"> 7,800 </span></td></tr> 
														  <tr class="down"><th scope="row"><em>3.</em><a href="/item/main.naver?code=035720" onclick="clickcr(this, &quot;boa.list&quot;, &quot;035720&quot;, &quot;3&quot;, event);">카카오</a></th><td>55,100</td><td><em class="bu_p bu_pdn"><span class="blind">하락</span></em><span class="tah p11 nv01"> 400 </span></td></tr> 
														  <tr class="up"><th scope="row"><em>4.</em><a href="/item/main.naver?code=000660" onclick="clickcr(this, &quot;boa.list&quot;, &quot;000660&quot;, &quot;4&quot;, event);">SK하이닉스</a></th><td>79,300</td><td><em class="bu_p bu_pup"><span class="blind">상승</span></em><span class="tah p11 red02"> 400 </span></td></tr> 
														  <tr class="down"><th scope="row"><em>5.</em><a href="/item/main.naver?code=051910" onclick="clickcr(this, &quot;boa.list&quot;, &quot;051910&quot;, &quot;5&quot;, event);">LG화학</a></th><td>672,000</td><td><em class="bu_p bu_pdn"><span class="blind">하락</span></em><span class="tah p11 nv01"> 7,000 </span></td></tr> 
														 </tbody> 
														</table>  
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
</body>
</html>