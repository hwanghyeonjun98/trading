<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩 | 데이터 조회</title>
	<%@ include file="/WEB-INF/views/trading/inc/defualt_css.jsp" %>
	<link rel="stylesheet" href="/css/dataview.css">
</head>
<body>
	<div class="background-wrap">
		<%@ include file="/WEB-INF/views/trading/inc/header.jsp" %>
		<main class="p-3">
			<section>
				<article>
					<ul>
						<li></li>
					</ul>
					<button type="button" class="data-view-btn">usdkrw내역</button>
					<h4><span class="data-name">a</span>내역</h4>
					<table id="data-table" class="table table-hover table-striped position-relative">
						<thead class="table-secondary">
							<tr>
								<td class="dates">
									날짜
									<button type="button" class="sort-btn"><i class="bi bi-arrow-down-up"></i></button>
								</td>
								<td class="closes">종가</td>
								<td class="opens">오픈</td>
								<td class="highs">고가</td>
								<td class="lows">저가</td>
								<td class="volumes">거래량</td>
								<td class="changes">변동</td>
							</tr>
						</thead>
						<tbody>
						</tbody>
					</table>
					<small>
						데이터 출처 : investing
					</small>
				</article>
			</section>
		</main>
		<%@ include file="/WEB-INF/views/trading/inc/footer.jsp" %>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
	<script src="/js/common.js"></script>
	<script src="/js/data_ajax.js"></script>
	<script src="/js/data_sort.js"></script>
</body>
</html>