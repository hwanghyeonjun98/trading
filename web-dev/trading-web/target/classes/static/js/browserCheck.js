const agent = navigator.userAgent.toLowerCase();

if ((navigator.appName == 'Netscape' && navigator.userAgent.search('Trident') != -1) || (agent.indexOf("msie") != -1)) {
	alert("익스플로러는 홈페이지 사용이 불가능합니다.\n크롬, 엣지, 웨일, 파이어폭스, 사파리 브라우저에서 접속해 주세요.");
	location.href = "../error/browser_info.jsp";
}
console.log(agent);