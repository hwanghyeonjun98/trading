<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩 | 데이터 조회</title>
	<%-- 기본적으로 불러와야 하는 것--%>
	<%@ include file="/WEB-INF/views/trading/inc/defualt_css.jsp" %>
	<link rel="stylesheet" href="/css/dataview.css">
</head>
<body>
	<div class="background-wrap">
		<%-- haeder include--%>
		<%@ include file="/WEB-INF/views/trading/inc/header.jsp" %>
		<%-- haeder include--%>
		<main class="p-3 sub-page">
			<section>
				<article>
					<%-- 메뉴 영역 --%>
					<nav class="data-menu">
						<div class="menu-area">
							<div class="menu-title">
								<h3 class="h6 mb-0">환율</h3>
								<span class="icon-span">
									<i class="bi bi-arrow-bar-down"></i>
								</span>
							</div>
							<div class="menu-content">
								<ul class="currencies">
								</ul>
							</div>
						</div>
						<div class="menu-area">
							<div class="menu-title">
								<h3 class="h6 mb-0">세계지수</h3>
								<span class="icon-span">
									<i class="bi bi-arrow-bar-down"></i>
								</span>
							</div>
							<div class="menu-content">
								<ul class="indices">
								</ul>
							</div>
						</div>
						<div class="menu-area">
							<div class="menu-title">
								<h3 class="h6 mb-0">원자재</h3>
								<span class="icon-span">
									<i class="bi bi-arrow-bar-down"></i>
								</span>
							</div>
							<div class="menu-content">
								<ul class="commodities">
								</ul>
							</div>
						</div>
						<div class="menu-area">
							<div class="menu-title">
								<h3 class="h6 mb-0">채권</h3>
								<span class="icon-span">
									<i class="bi bi-arrow-bar-down"></i>
								</span>
							</div>
							<div class="menu-content">
								<ul class="rates_bonds">
								</ul>
							</div>
						</div>
						<div class="menu-area">
							<div class="menu-title">
								<h3 class="h6 mb-0">암호화폐</h3>
								<span class="icon-span">
									<i class="bi bi-arrow-bar-down"></i>
								</span>
							</div>
							<div class="menu-content">
								<ul class="conins">
								</ul>
							</div>
						</div>
					</nav>
					<%-- 메뉴 영역 --%>
					<h4 class="data-title h3 mt-4 mb-3 p-2 px-4"><span class="data-name">AED/KRW</span> 내역</h4>
					<%-- 차트 영역 --%>
					<div id="chart-area"></div>
					<%-- 차트 영역 --%>
					<div class="date-search-form">
						<form name="dateSearchFrm" id="dateSearchFrm" method="post">
							<label for="startDate">시작 날짜</label>
							<input type="date" name="startDate" id="startDate" min="2020-01-01" max="">
							<label for="endDate">끝 날짜</label>
							<input type="date" name="endDate" id="endDate" max="" value="">
							<button type="submit"><i class="bi bi-search"></i></button>
						</form>
					</div>
					<%-- 데이터 영역 --%>
					<table id="data-table" class="table table-hover table-striped position-relative" data-table="aedkrw">
						<thead class="table-secondary">
							<tr>
								<th class="dates">
									날짜
									<button type="button" class="sort-btn sorted"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th class="closes">
									종가
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th class="opens">
									오픈
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th class="highs">
									고가
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th class="lows">
									저가
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th class="volumes">
									거래량
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th class="changes">
									변동
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
							</tr>
						</thead>
						<tbody>
							<c:forEach items="${defaultData}" var="defaultData">
								<tr>
									<td>${defaultData.dates}</td>
									<td>${defaultData.closes}</td>
									<td>${defaultData.opens}</td>
									<td>${defaultData.highs}</td>
									<td>${defaultData.lows}</td>
									<td>${defaultData.volumes}</td>
									<td>${defaultData.changes}</td>
								</tr>
							</c:forEach>
						</tbody>
					</table>
					<%-- 데이터 영역 --%>
					<small>
						데이터 출처 : investing
					</small>
				</article>
			</section>
		</main>
		<%-- footer include--%>
		<%@ include file="/WEB-INF/views/trading/inc/footer.jsp" %>
		<%-- footer include--%>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
	<script src="/js/common.js"></script>
	<script src="/js/data_list.js"></script>
	<script src="/js/chart_js.js"></script>
	<script src="/js/data_ajax.js"></script>
	<script src="/js/data_sort.js"></script>
</body>
</html>