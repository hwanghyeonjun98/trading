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
		<main class="px-3 py-4">
			<section class="main-list">
				<article class="w-75">
					<div id="ai-trading-area" class="pe-4">
						<div class="table-title">
							<h3 class="h3 pe-2">AI 실시간 트레이딩</h3>
							<small>트레이딩 시간 : 9:00 ~ 15:00</small>
							<div class="snap ms-auto">TIME : <span id="current" class="display"></span></div>
						</div>
						<table id="trading-data-table" class="table table-hover table-striped table-sort">
							<colgroup>
								<col style="width: 180px">
								<col style="width: 160px">
								<col style="width: 150px">
								<col style="width: 220px">
								<col style="width: 220px">
								<col style="width: 220px">
								<col style="width: 220px">
							</colgroup>
							<thead class="table-secondary">
								<tr>
									<th>종목코드</th>
									<th>종목명</th>
									<th>보유수량</th>
									<th>평단가</th>
									<th>평가금액</th>
									<th>수익율</th>
									<th>장부금액</th>
								</tr>
							</thead>
							<tbody>
							</tbody>
						</table>
					</div>
				</article>
				<article class="recommend-list w-25">
					<div class="clear-wrapper">
					</div>
					<div class="recommendation-keywords-container">
						<div class="titlecu mt-0"><h3>환율 검색 추천</h3></div>
						<hr>
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
						<div class="titlecu"><h3>세계지수 검색 추천</h3></div>
						<hr>
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
				</article>
			</section>
			<article>
				<a href="https://deepsearch-jira.atlassian.net/servicedesk/customer/kb/view/636583937" class="banner" target="_blank" rel="noopener noreferrer">
					<img src="https://deepsearchimages.wpcomstaging.com/wp-content/uploads/cards/2022/11/banner_20221124-20221124-053132.png" alt="[DAP] 경제 지표 개선 공지">
				</a>
			</article>
			<section class="main-list">
				<h3 class="main_title">주식 관련 기사 추천</h3>
				<div class="d-flex justify-content-start align-items-start w-100">
					<article class="w-75">
						<div class="groups d-flex justify-content-start align-items-start flex-wrap">
							<div class="economic-indicator">
								<div class="jot"></div>
								<div id="root">
								</div>
								<div class="indicator-name">
									<img src="https://imgnews.pstatic.net/image/018/2022/12/16/0005388149_003_20221216095701914.jpg?type=w540" width="255" height="285">
									<hr class='hr-solid'>
									<span>국내 이슈</span>
								</div>
								<div class="main-value">주제 :<span class="change-rate_pos">한국전력</span>
								</div>
								<div class="sub-value">기사 제목 :<span class="change-rate_pos">9부능선 넘은 한전법 개정안…'디폴트 위기' 한전 한숨 돌렸다</span>
								</div>
								<div class="date-info">
									<hr class='hr-solid'>
									<button class="btn btn-success" onClick="location.href='https://finance.naver.com/item/news_read.naver?article_id=0005388149&office_id=018&code=015760&sm=title_entity_id.basic'">
										링크로 이동
									</button>
								</div>
							</div>
							<div class="economic-indicator">
								<div class="indicator-name">
									<img src="https://imgnews.pstatic.net/image/008/2022/12/16/0004829736_001_20221216072901029.jpg?type=w540" width="255" height="285">
									<hr class='hr-solid'>
									<span>해외 이슈</span>
								</div>
								<div class="main-value">주제 :<span class="change-rate_neg">금리</span></div>
								<div class="sub-value">기사 제목 :<span class="change-rate_neg">'고금리→침체' 우려에 증시급락..."소비 불안"[뉴욕마감]</span>
								</div>
								<div class="date-info">
									<hr class='hr-solid'>
									<button class="btn btn-success" onClick="location.href='https://finance.naver.com/news/news_read.naver?article_id=0004829736&office_id=008&mode=mainnews&type=&date=2022-12-16&page=1'">
										링크로 이동
									</button>
								</div>
							</div>
							<div class="economic-indicator">
								<div class="indicator-name">
									<img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F001%2F2022%2F10%2F05%2FPYh3022100502140001300_P4_20221005092413890.jpg&type=l340_165" width="255" height="285">
									<hr class='hr-solid'>
									<span>환율 관련</span>
								</div>
								<div class="main-value">주제 :<span class="change-rate_neg">환율</span></div>
								<div class="sub-value">기사 제목 :<span class="change-rate_neg">코스피 하락, 환율 상승 출발</span></div>
								<hr class='hr-solid'>
								<button class="btn btn-success" onClick="location.href='https://newsis.com/view/?id=NISI20221216_0019595479'">
									링크로 이동
								</button>
							</div>
							<div class="economic-indicator">
								<div class="indicator-name">
									<img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjExMTJfMTAw%2FMDAxNjY4MjE4MzIxMTAw.uN064CZvfnaj08SWljDs-jm4--M_pjT_9Sk3lP25XpEg.rx2QFgxITz7Kj4joJg5LZkwNq6nH1vVcDvv-WZJ3aZwg.JPEG.p9573198%2F0006452791%25A3%25DF002%25A3%25DF20221112052801742.jpg&type=a340" width="255" height="285">
									<hr class='hr-solid'>
									<span>비트코인 관련</span>
								</div>
								<div class="main-value">주제 :<span class="change-rate_neg">FTX 사태</span></div>
								<div class="sub-value">기사 제목 :<span class="change-rate_neg">뱅크런은 어떻게 시작됐나…FTX 사태 주요 일지</span></div>
								<hr class='hr-solid'>
								<button class="btn btn-success " onClick="location.href='http://www.coindeskkorea.com/news/articleView.html?idxno=82076'">
									링크로 이동
								</button>
							</div>
						</div>
						<div>
							<h3 class="mb-0">추천 뉴스</h3>
							<hr>
							<ul class="ps-2">
								<c:forEach items="${nnews}" var="nnews">
									<li>
										<a href="${nnews.newsLink}" class="news-link">
											<h5 class="hove">${nnews.newsName}</h5>
											<p class="llong">${nnews.news}</p>
										</a>
									</li>
								</c:forEach>
							</ul>
						</div>
					</article>
					<article class="w-25">
						<div class="chartFrame">
							<h3>코스피 지수 현황</h3>
							<hr>
							<div id="chart-area">
							</div>
							<h3>시가 총액 상위</h3>
							<hr/>
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
									<li>10.셀트리온</li>
								</ul>
							</div>
						</div>
					</article>
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
	<script src="/js/index_chart.js"></script>
	<script src="/js/index_ajax.js"></script>
	<script src="/js/aiTrading.js"></script>
</body>
</html>