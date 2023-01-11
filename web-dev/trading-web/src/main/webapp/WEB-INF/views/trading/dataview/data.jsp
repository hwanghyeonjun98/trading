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
	<c:if test="${error_msg != null}">
		<script>
			alert("${error_msg}");
			location.href = "/";
		</script>
	</c:if>
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
							<div class="menu-title" tabindex="0">
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
							<div class="menu-title" tabindex="0">
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
							<div class="menu-title" tabindex="0">
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
							<div class="menu-title" tabindex="0">
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
							<div class="menu-title" tabindex="0">
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
						<%--	재무재표 검색	--%>
						<div class="fs-data-search d-flex justify-content-start align-items-center">
							<label for="fsData" class="m-0 pe-1">재무재표 검색 : </label>
							<input type="text" name="fsData" id="fsData" class="form-control w-25 me-2" list="fs-data-list" placeholder="종목 코드 또는 종목명을 입력하세요." autocomplete="off">
							<datalist id="fs-data-list">
								<option value=""></option>
							</datalist>

							<button type="button" class="btn btn-outline-success" id="fsModalBtn" data-bs-toggle="modal" data-bs-target="#fsmodal">검색</button>
						</div>
						<%--	재무재표 검색	--%>
					</nav>
					<%-- 메뉴 영역 --%>
					<h4 class="data-title h3 mt-4 mb-3 p-2 px-4">
						<span class="data-name">AED/KRW</span>내역
						<small class="data-category"></small>
					</h4>
					<%-- 차트 영역 --%>
					<p class="text-end">
						<small>2020-01-01 ~ 현재</small>
					</p>
					<div id="chart-area"></div>
					<%-- 차트 영역 --%>
					<div class="date-search-form w-100 my-3">
						<form name="dateSearchFrm" id="dateSearchFrm" method="post">
							<div>
								날짜 검색 :
							</div>
							<div class="col-sm-2">
								<label for="startDate" class="visually-hidden">시작 날짜</label>
								<input type="date" name="startDate" id="startDate" class="form-control" min="2020-01-01">
							</div>
							<div class="col-sm-2">
								<label for="endDate" class="visually-hidden">끝 날짜</label>
								<input type="date" name="endDate" id="endDate" class="form-control" max="" value="">
							</div>
							<button type="submit" class="btn btn-outline-success btn-sm"><i class="bi bi-search"></i>
							</button>
						</form>
					</div>
					<%-- 데이터 영역 --%>
					<p class="text-end mobile-show"><b><i class="bi bi-arrow-left-right"></i> 옆으로 스크롤</b></p>
					<div class="table-wrap">
						<table id="data-table" class="table table-hover table-striped table-sort" data-table="${defaultDataName}">
							<thead class="table-secondary">
								<tr>
									<th id="dates" class="order-by-desc">
										날짜
										<button type="button" class="sort-btn sorted"><i class="bi bi-arrow-down-up"></i>
										</button>
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
					</div>
					<%-- 데이터 영역 --%>
					<p class="text-end">
						<small>
							데이터 출처 : investing
						</small>
					</p>
				</article>
			</section>
		</main>

			<div class="modal fade" tabindex="-1" id="fsmodal">
				<div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable" >
					<div class="modal-content">
						<div class="modal-header mb-3">
							<h5 class="modal-title">
								재무제표
							</h5>
							<button type="button" class="btn-close modal-close" data-bs-dismiss="modal" aria-label="Close"></button>
						</div>
						<div class="modal-body p-0">
							<div class="m-3 mt-0">
								<div class="loading-div">
									<div class="d-flex justify-content-center align-items-center flex-column">
										<div class="spinner-border" role="status">
											<span class="visually-hidden">Loading...</span>
										</div>
										<p>불러오는 중</p>
									</div>
								</div>
								<table id="fsTable" class="table table-hover table-striped">
									<thead class="table-secondary">
										<tr>
											<th>날짜</th>
											<th>재무제표<br>유동자산</th>
											<th>재무제표<br>비유동자산</th>
											<th>재무제표<br>자산총계</th>
											<th>재무제표<br>유동부채</th>
											<th>재무제표<br>비유동부채</th>
											<th>재무제표<br>부채총계</th>
											<th>재무제표<br>자본금</th>
											<th>재무제표<br>이익잉여금</th>
											<th>재무제표<br>자본총계</th>
											<th>재무제표<br>매출액</th>
											<th>재무제표<br>영업이익</th>
											<th>재무제표<br>법인세차감전 순이익</th>
											<th>재무제표<br>당기순이익</th>
											<th>연결재무제표<br>유동자산</th>
											<th>연결재무제표<br>비유동자산</th>
											<th>연결재무제표<br>자산총계</th>
											<th>연결재무제표<br>유동부채</th>
											<th>연결재무제표<br>비유동부채</th>
											<th>연결재무제표<br>부채총계</th>
											<th>연결재무제표<br>자본금</th>
											<th>연결재무제표<br>이익잉여금</th>
											<th>연결재무제표<br>자본총계</th>
											<th>연결재무제표<br>매출액</th>
											<th>연결재무제표<br>영업이익</th>
											<th>연결재무제표<br>법인세차감전 순이익</th>
											<th>연결재무제표<br>당기순이익</th>
										</tr>
									</thead>
									<tbody>
									</tbody>
								</table>
							</div>
						</div>
						<div class="modal-footer">
							<button type="button" class="btn btn-secondary btn-sm modal-close" data-bs-dismiss="modal">Close</button>
						</div>
					</div>
				</div>
			</div>
		<%-- footer include--%>
		<%@ include file="/WEB-INF/views/trading/inc/footer.jsp" %>
		<%-- footer include--%>
	</div>
	<button type="button" class="top-to-btn">
		<i class="bi bi-arrow-up-circle-fill"></i>
	</button>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
	<script src="/js/common.js"></script>
	<script src="/js/data_list.js"></script>
	<script src="/js/chart_js.js"></script>
	<script src="/js/data_ajax.js"></script>
	<script src="/js/stock_search.js"></script>
	<script src="/js/table-sort.js"></script>
</body>
</html>