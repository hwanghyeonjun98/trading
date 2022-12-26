<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<header class="p-3">
	<h1 class="h2 mb-0 d-flex justify-content-start align-items-center">
		<a href="/">AITRADING</a>
	</h1>
	<nav class="header-nav">
		<div class="mobile-show">
			<button type="button" class="header-menu-btn">
				<i class="bi bi-list"></i>
			</button>
		</div>
		<div class="login-btn-area">
			<c:if test="${userAccount == null}">
				<a href="/login" class="login-btn">로그인</a>
			</c:if>
			<c:if test="${userAccount != null}">
				<button type="button" class="logout-btn">로그아웃</button>
			</c:if>
		</div>
		<ul class="header-menu-list">
			<li><a href="/" class="text-uppercase">HOME</a></li>
			<li><a href="/dataview/data" class="text-uppercase">DATA</a></li>
<%--			<li><a href="/developer/developer_info" class="text-uppercase">developer</a></li>--%>
		</ul>
	</nav>
</header>