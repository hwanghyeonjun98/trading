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
					<h4 class="data-title h3 mt-4 mb-3 p-2 px-4"><span class="data-name">AED/KRW</span>내역</h4>
					<%-- 차트 영역 --%>
					<div id="chart-area"></div>
					<%-- 차트 영역 --%>
					<div class="date-search-form w-100 my-3">
						<form name="dateSearchFrm" id="dateSearchFrm" method="post">
							<div>
								날짜 검섹 :
							</div>
							<div class="col-sm-2">
								<label for="startDate" class="visually-hidden">시작 날짜</label>
								<input type="date" name="startDate" id="startDate" class="form-control" min="2020-01-01">
							</div>
							<div class="col-sm-2">
								<label for="endDate" class="visually-hidden">끝 날짜</label>
								<input type="date" name="endDate" id="endDate" class="form-control" max="" value="">
							</div>
							<button type="submit" class="btn btn-outline-success btn-sm"><i class="bi bi-search"></i></button>
						</form>
					</div>
					<%-- 데이터 영역 --%>
					<table id="data-table" class="table table-hover table-striped position-relative table-sort" data-table="aedkrw">
						<thead class="table-secondary">
							<tr>
								<th id="dates" class="order-by-desc">
									날짜
									<button type="button" class="sort-btn sorted"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th id="closes" class="order-by-desc">
									종가
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th id="opens" class="order-by-desc">
									오픈
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th id="highs" class="order-by-desc">
									고가
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th id="lows" class="order-by-desc">
									저가
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th id="volumes" class="order-by-desc">
									거래량
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
								<th id="changes" class="order-by-desc">
									변동
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</th>
							</tr>
						</thead>
						<tbody>
							<c:forEach items="${dataList}" var="dataList">
								<tr>
									<td>${dataList.dates}</td>
									<td>${dataList.closes}</td>
									<td>${dataList.opens}</td>
									<td>${dataList.highs}</td>
									<td>${dataList.lows}</td>
									<td>${dataList.volumes}</td>
									<td>${dataList.changes}%</td>
								</tr>
							</c:forEach>
						</tbody>
					</table>
					<%-- 데이터 영역 --%>
					<p class="text-end">
						<small>
							데이터 출처 : investing
						</small>
					</p>
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
	<script src="/js/table-sort.js"></script>
</body>
</html>