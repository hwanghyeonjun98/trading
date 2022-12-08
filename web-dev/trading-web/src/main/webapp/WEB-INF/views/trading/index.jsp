<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!doctype html>
<html lang="ko">

<link rel="stylesheet" href="/css/index.css">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>트레이딩</title>
	<%@ include file="/WEB-INF/views/trading/inc/defualt_css.jsp" %>
</head>
<body>
	<div class="background-wrap">
		<%@ include file="/WEB-INF/views/trading/inc/header.jsp" %>
		<main class="p-3">
			<section>
				<article>
					<div class="search-bar-content">
						<div class="icon-search">
							<div>
								<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="injected-svg" data-src="/icons/icon-search.svg" xmlns:xlink="http://www.w3.org/1999/xlink">
								<path id="icon-search-170" fill="#181A1E" fill-rule="evenodd" d="M17.1760252,15.7618116 L21.7071068,20.2928932 C22.0976311,20.6834175 22.0976311,21.3165825 21.7071068,21.7071068 C21.3165825,22.0976311 20.6834175,22.0976311 20.2928932,21.7071068 L15.7618116,17.1760252 C14.3145189,18.3182963 12.4868697,19 10.5,19 C5.80557963,19 2,15.1944204 2,10.5 C2,5.80557963 5.80557963,2 10.5,2 C15.1944204,2 19,5.80557963 19,10.5 C19,12.4868697 18.3182963,14.3145189 17.1760252,15.7618116 Z M15.1597589,15.0317433 C16.2986171,13.8609174 17,12.2623671 17,10.5 C17,6.91014913 14.0898509,4 10.5,4 C6.91014913,4 4,6.91014913 4,10.5 C4,14.0898509 6.91014913,17 10.5,17 C12.2623671,17 13.8609174,16.2986171 15.0317433,15.1597589 C15.0509347,15.1367843 15.071318,15.1144685 15.0928932,15.0928932 C15.1144685,15.071318 15.1367843,15.0509347 15.1597589,15.0317433 Z"></path>
								</svg>
							</div>
						</div>
						<textarea autocomplete="off" id="search-input" placeholder="환율이 궁금한 국가를 검색하세요!" class="" spellcheck="false" style="height: 50px;"></textarea>
						<div class="clear-wrapper">	
						</div>
					</div>
					<div class="recommendation-keywords-container">
						<div class="titlecu">환율 검색 추천</div>
						<div class="keywords-container-wrapper">
							<div class="keywords-contents">
								<a href="/analytics/compute?input=%EA%B2%BD%EA%B8%B0%EB%B0%A9%EC%96%B4%20%EA%B4%80%EB%A0%A8%20%EA%B8%B0%EC%97%85&amp;avds=false">
									<div class="keyword item">미국 USD</div>
								</a>
								<a href="/analytics/compute?input=%EA%B3%A0%EB%B0%B0%EB%8B%B9%20%EA%B4%80%EB%A0%A8%20%EA%B8%B0%EC%97%85%20and%20(%EC%83%81%EC%9E%A5%20%EA%B8%B0%EC%97%85)&amp;avds=false">
									<div class="keyword item">유럽연합 EUR</div>
								</a>
								<a href="/analytics/compute?input=%22*K641*%22%20%EC%82%B0%EC%97%85%20%EA%B8%B0%EC%97%85%20and%20%EC%98%81%EC%97%85%EC%9D%B4%EC%9D%B5%20%3E%2010000000000&amp;avds=false">
									<div class="keyword item">일본 JPY (100엔)</div>
								</a>
								<a href="/analytics/compute?input=%EB%82%98%EC%9D%B4%EC%8A%A4%ED%8F%89%EA%B0%80%EC%A0%95%EB%B3%B4%20%EC%BD%94%EB%A6%AC%EC%95%84%ED%81%AC%EB%A0%88%EB%94%A7%EB%B7%B0%EB%A1%9C%20%EB%A7%A4%EC%B6%9C%20%EC%98%81%EC%97%85%EC%9D%B4%EC%9D%B5%20%EB%8B%B9%EA%B8%B0%EC%88%9C%EC%9D%B4%EC%9D%B5%202018-2021&amp;avds=false">
									<div class="keyword item">중국 CNY</div>
								</a>
								<a href="/analytics/compute?input=SPC%EC%82%BC%EB%A6%BD%20%EB%A7%A4%EC%B6%9C%20%EC%98%81%EC%97%85%EC%9D%B4%EC%9D%B5%20%EB%8B%B9%EA%B8%B0%EC%88%9C%EC%9D%B4%EC%9D%B5%202018-2021&amp;avds=false">
									<div class="keyword item">대만 TWD</div>
								</a>
								<a href="/analytics/compute?input=DocumentSearch(%22news%22%2C%22economy%22%2C%22title%3A((%EB%A0%88%EA%B3%A0%EB%9E%9C%EB%93%9C))%22%2Ccount%3D100)&amp;avds=false">
									<div class="keyword item">영국 GBP</div>
								</a>
								<a href="/analytics/compute?input=DocumentSearch(%22news%22%2C%22economy%22%2C%22title%3A((SK%20C%26C))%22%2Ccount%3D100)&amp;avds=false">
									<div class="keyword item">캐나다 CAD</div>
								</a>
								<a href="/analytics/compute?input=%EC%A0%95%EC%9C%A1%EA%B0%81%20%EB%A7%A4%EC%B6%9C%20%EC%98%81%EC%97%85%EC%9D%B4%EC%9D%B5%20%EB%8B%B9%EA%B8%B0%EC%88%9C%EC%9D%B4%EC%9D%B5%202018-2021&amp;avds=false">
									<div class="keyword item">홍콩 HKD</div>
								</a>
								<a href="/analytics/compute?input=DocumentSearch(%22research%22%2CNone%2C%22securities.name%3A%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8E%98%EC%9D%B4%22)&amp;avds=false">
									<div class="keyword item">덴마크 DKK</div>
								</a>
								<a href="/analytics/compute?input=DocumentSearch(%22research%22%2CNone%2C%22securities.name%3A%ED%95%9C%EA%B5%AD%EC%A0%84%EB%A0%A5%22)&amp;avds=false">
									<div class="keyword item">튀르키예 TRY</div>
								</a>
								<a href="/analytics/compute?input=%EC%97%90%EC%8A%A4%EC%97%90%EC%9D%B4%EC%97%A0%EC%A7%80%EC%97%94%ED%84%B0%ED%85%8C%EC%9D%B8%EB%A8%BC%ED%8A%B8%20%EB%A7%A4%EC%B6%9C%20%EC%98%81%EC%97%85%EC%9D%B4%EC%9D%B5%20%EB%8B%B9%EA%B8%B0%EC%88%9C%EC%9D%B4%EC%9D%B5%202018-2021&amp;avds=false">
									<div class="keyword item">태국 THB</div>
								</a>
								<a href="/analytics/compute?input=%EC%98%B5%ED%8B%B0%EC%BD%94%EC%96%B4%20%EB%A7%A4%EC%B6%9C%20%EC%98%81%EC%97%85%EC%9D%B4%EC%9D%B5%20%EB%8B%B9%EA%B8%B0%EC%88%9C%EC%9D%B4%EC%9D%B5%202018-2021&amp;avds=false">
									<div class="keyword item">필리핀 PHP</div>
								</a>
							</div>
						</div>
					</div>
					<a href="https://deepsearch-jira.atlassian.net/servicedesk/customer/kb/view/636583937" class="banner" target="_blank" rel="noopener noreferrer">
						<img src="https://deepsearchimages.wpcomstaging.com/wp-content/uploads/cards/2022/11/banner_20221124-20221124-053132.png" alt="[DAP] 경제 지표 개선 공지">
					</a>
					
					<h2 class="main_title">국내 금융시장 주요 지표</h2>
					<div class="main_gr">
						<div class="economic-indicator">
							<div class="indicator-name">
								<a href="/analytics/economic-indicator/BOK%3A802Y001.0001000">코스피</a>
							</div>
							<div class="main-value"><span class="change-rate_neg">2,419.32</span>
							</div>
							<div class="sub-value">3일 전 대비<span class="change-rate_neg">-0.62%</span></div>
							<div class="sub-value">전년도 대비<span class="change-rate_neg">-18.5%</span></div>
							<div class="date-info"><div class="cycle">주기: Daily</div>
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
							<div class="date-info"><div class="cycle">주기: Daily</div>
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
							<div class="date-info"><div class="cycle">주기: Daily</div>
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
							<div class="date-info"><div class="cycle">주기: Daily</div>
							<div class="date">2022. 12. 05</div>
							</div>
						</div>	
					</div>

					<div class="chartFrame">
						<div id="quotesBoxChartTimeFrames" class="timePeriods">
							<span data-time-frame="1day" class="selected">1일 코스피 현재 지수</span>
							<a href="/indices/kospi-chart" class="js-chart-link quotesboxLinkIcon"></a></div>
							<div id="quotesBoxChart" class="quotesChartWrapper" data-highcharts-chart="0">
								<div class="highcharts-container" id="highcharts-0" style="position: relative; overflow: hidden; width: 298px; height: 140px; text-align: left; line-height: normal; z-index: 0; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); font-family: Arial, sans-serif;"><svg version="1.1" style="font-family:Arial, sans-serif;font-size:12px;" xmlns="http://www.w3.org/2000/svg" width="298" height="140">
									<desc>Created with Highcharts 4.0.4 /Highstock 2.0.4</desc>
									<defs>
										<clipPath id="highcharts-1"><rect x="0" y="0" width="297" height="150"></rect>
										</clipPath></defs>
										<rect x="0" y="0" width="298" height="140" strokeWidth="0" fill="transparent" class=" highcharts-background"></rect><g class="highcharts-grid" zIndex="1"></g><g class="highcharts-axis" zIndex="1"></g>
									<g class="highcharts-grid" zIndex="1">
										<path fill="none" d="M 1 113.5 L 298 113.5" stroke="#ececec" stroke-width="1" zIndex="1" opacity="1"></path>
										<path fill="none" d="M 1 40.5 L 298 40.5" stroke="#ececec" stroke-width="1" zIndex="1" opacity="1"></path>
										<path fill="none" d="M 1 3.5 L 298 3.5" stroke="#ececec" stroke-width="1" zIndex="1" opacity="1"></path>
										<path fill="none" d="M 1 77.5 L 298 77.5" stroke="#ececec" stroke-width="1" zIndex="1" opacity="1"></path>
										<path fill="none" d="M 1 150.5 L 298 150.5" stroke="#ececec" stroke-width="1" zIndex="1" opacity="1"></path></g><g class="highcharts-axis" zIndex="2"></g>
										<path fill="none" d="M 267.5 0 L 267.5 150" stroke="#C0C0C0" stroke-width="1" zIndex="2" visibility="hidden"></path>
										<path fill="none" d="M 1 37.5 L 298 37.5" stroke="#C0C0C0" stroke-width="1" zIndex="2" visibility="hidden"></path>
										<rect x="298" y="73.77165354330788" width="0" height="15" fill="#C0C0C0" stroke="#C0C0C0" stroke-width="1" zIndex="2"></rect>
										<g class="highcharts-series-group" zIndex="3">
											<g class="highcharts-series" visibility="visible" zIndex="0.1" transform="translate(1,0) scale(1 1)" clip-path="url(#highcharts-1)">
												<path fill="rgba(0, 96, 152, 0.1)" d="M 0 24.257217847770505 L 3.7594936708967364 18.818897637798443 L 7.518987341793473 19.406824146984263 L 11.278481012690209 19.406824146984263 L 15.037974683586945 16.54068241470179 L 18.79746835448368 16.54068241470179 L 22.556962025380418 81.35958005249368 L 26.316455696277153 80.25721784777197 L 30.07594936717389 45.2020997375332 L 33.83544303807063 66.29396325459571 L 37.59493670896736 33.29658792651061 L 41.3544303798641 76.06824146981809 L 45.113924050760836 71.6587926509212 L 48.873417721657574 51.595800524937204 L 52.632911392554306 85.69553805774402 L 56.392405063451044 102.15748031495994 L 60.15189873434778 97.60104986876661 L 63.91139240524452 94.14698162729832 L 67.67088607614126 93.77952755905552 L 71.43037974703799 97.9685039370094 L 75.18987341793472 96.57217847769144 L 78.94936708883147 104.21522309711361 L 82.7088607597282 78.49343832021121 L 86.46835443062494 68.71916010498883 L 90.22784810152167 55.78477690288774 L 93.9873417724184 32.63517060367826 L 97.74683544331515 32.047244094489116 L 101.50632911421188 46.37795275590817 L 105.26582278510861 22.713910761156086 L 109.02531645600536 32.708661417324805 L 112.78481012690209 36.60367454068579 L 116.54430379779883 16.981627296591142 L 120.30379746869556 27.93175853018512 L 124.0632911395923 47.03937007874052 L 127.82278481048904 43.732283464568695 L 131.58227848138577 57.10761154855915 L 135.34177215228252 60.78215223097378 L 139.10126582317923 73.93700787401787 L 142.86075949407598 70.77690288713916 L 146.62025316497272 68.64566929133893 L 150.3797468350273 66.00000000000281 L 154.13924050592402 76.50918635170744 L 157.89873417682077 84.5196850393724 L 161.6582278477175 84.07874015748305 L 165.41772151861423 76.28871391076109 L 169.17721518951097 76.95013123359679 L 172.93670886040772 82.75590551181165 L 176.69620253130444 108.18372703412113 L 180.45569620220118 99.58530183727038 L 184.21518987309793 84.29921259842605 L 187.97468354399464 74.15748031496088 L 191.7341772148914 61.14960629921323 L 195.49367088578813 72.17322834645711 L 199.25316455668488 58.72440944882011 L 203.0126582275816 48.362204724411924 L 206.77215189847834 36.30971128609289 L 210.5316455693751 34.03149606299287 L 214.2911392402718 28.00524934383502 L 218.05063291116855 10.000000000001336 L 221.8101265820653 14.923884514437475 L 225.569620252962 32.92913385827116 L 229.32911392385876 35.20734908136782 L 233.0886075947555 25.874015748034807 L 236.84810126565222 13.601049868769422 L 240.60759493654896 22.346456692916632 L 244.3670886074457 17.128608923887583 L 248.12658227834243 29.622047244095995 L 251.88607594923917 31.312335958006855 L 255.64556962013592 35.06036745407138 L 259.40506329103266 33.59055118110352 L 263.1645569619294 45.422572178479555 L 266.9240506328261 37.26509186351815 L 270.68354430372284 38.734908136486 L 274.4430379746196 28.00524934383502 L 278.20253164551633 32.41469816273191 L 281.9620253164131 31.238845144360297 L 285.7215189873098 42.40944881890063 L 289.48101265820657 73.27559055118218 L 293.24050632910325 87.60629921260121 L 297 80.77165354330788 L 297 150 L 0 150" zIndex="0"></path><path fill="none" d="M 0 24.257217847770505 L 3.7594936708967364 18.818897637798443 L 7.518987341793473 19.406824146984263 L 11.278481012690209 19.406824146984263 L 15.037974683586945 16.54068241470179 L 18.79746835448368 16.54068241470179 L 22.556962025380418 81.35958005249368 L 26.316455696277153 80.25721784777197 L 30.07594936717389 45.2020997375332 L 33.83544303807063 66.29396325459571 L 37.59493670896736 33.29658792651061 L 41.3544303798641 76.06824146981809 L 45.113924050760836 71.6587926509212 L 48.873417721657574 51.595800524937204 L 52.632911392554306 85.69553805774402 L 56.392405063451044 102.15748031495994 L 60.15189873434778 97.60104986876661 L 63.91139240524452 94.14698162729832 L 67.67088607614126 93.77952755905552 L 71.43037974703799 97.9685039370094 L 75.18987341793472 96.57217847769144 L 78.94936708883147 104.21522309711361 L 82.7088607597282 78.49343832021121 L 86.46835443062494 68.71916010498883 L 90.22784810152167 55.78477690288774 L 93.9873417724184 32.63517060367826 L 97.74683544331515 32.047244094489116 L 101.50632911421188 46.37795275590817 L 105.26582278510861 22.713910761156086 L 109.02531645600536 32.708661417324805 L 112.78481012690209 36.60367454068579 L 116.54430379779883 16.981627296591142 L 120.30379746869556 27.93175853018512 L 124.0632911395923 47.03937007874052 L 127.82278481048904 43.732283464568695 L 131.58227848138577 57.10761154855915 L 135.34177215228252 60.78215223097378 L 139.10126582317923 73.93700787401787 L 142.86075949407598 70.77690288713916 L 146.62025316497272 68.64566929133893 L 150.3797468350273 66.00000000000281 L 154.13924050592402 76.50918635170744 L 157.89873417682077 84.5196850393724 L 161.6582278477175 84.07874015748305 L 165.41772151861423 76.28871391076109 L 169.17721518951097 76.95013123359679 L 172.93670886040772 82.75590551181165 L 176.69620253130444 108.18372703412113 L 180.45569620220118 99.58530183727038 L 184.21518987309793 84.29921259842605 L 187.97468354399464 74.15748031496088 L 191.7341772148914 61.14960629921323 L 195.49367088578813 72.17322834645711 L 199.25316455668488 58.72440944882011 L 203.0126582275816 48.362204724411924 L 206.77215189847834 36.30971128609289 L 210.5316455693751 34.03149606299287 L 214.2911392402718 28.00524934383502 L 218.05063291116855 10.000000000001336 L 221.8101265820653 14.923884514437475 L 225.569620252962 32.92913385827116 L 229.32911392385876 35.20734908136782 L 233.0886075947555 25.874015748034807 L 236.84810126565222 13.601049868769422 L 240.60759493654896 22.346456692916632 L 244.3670886074457 17.128608923887583 L 248.12658227834243 29.622047244095995 L 251.88607594923917 31.312335958006855 L 255.64556962013592 35.06036745407138 L 259.40506329103266 33.59055118110352 L 263.1645569619294 45.422572178479555 L 266.9240506328261 37.26509186351815 L 270.68354430372284 38.734908136486 L 274.4430379746196 28.00524934383502 L 278.20253164551633 32.41469816273191 L 281.9620253164131 31.238845144360297 L 285.7215189873098 42.40944881890063 L 289.48101265820657 73.27559055118218 L 293.24050632910325 87.60629921260121 L 297 80.77165354330788" stroke="rgb(132, 178, 218)" stroke-width="1" zIndex="1" stroke-linejoin="round" stroke-linecap="round"></path>
												<path fill="none" d="M -10 24.257217847770505 L 0 24.257217847770505 L 3.7594936708967364 18.818897637798443 L 7.518987341793473 19.406824146984263 L 11.278481012690209 19.406824146984263 L 15.037974683586945 16.54068241470179 L 18.79746835448368 16.54068241470179 L 22.556962025380418 81.35958005249368 L 26.316455696277153 80.25721784777197 L 30.07594936717389 45.2020997375332 L 33.83544303807063 66.29396325459571 L 37.59493670896736 33.29658792651061 L 41.3544303798641 76.06824146981809 L 45.113924050760836 71.6587926509212 L 48.873417721657574 51.595800524937204 L 52.632911392554306 85.69553805774402 L 56.392405063451044 102.15748031495994 L 60.15189873434778 97.60104986876661 L 63.91139240524452 94.14698162729832 L 67.67088607614126 93.77952755905552 L 71.43037974703799 97.9685039370094 L 75.18987341793472 96.57217847769144 L 78.94936708883147 104.21522309711361 L 82.7088607597282 78.49343832021121 L 86.46835443062494 68.71916010498883 L 90.22784810152167 55.78477690288774 L 93.9873417724184 32.63517060367826 L 97.74683544331515 32.047244094489116 L 101.50632911421188 46.37795275590817 L 105.26582278510861 22.713910761156086 L 109.02531645600536 32.708661417324805 L 112.78481012690209 36.60367454068579 L 116.54430379779883 16.981627296591142 L 120.30379746869556 27.93175853018512 L 124.0632911395923 47.03937007874052 L 127.82278481048904 43.732283464568695 L 131.58227848138577 57.10761154855915 L 135.34177215228252 60.78215223097378 L 139.10126582317923 73.93700787401787 L 142.86075949407598 70.77690288713916 L 146.62025316497272 68.64566929133893 L 150.3797468350273 66.00000000000281 L 154.13924050592402 76.50918635170744 L 157.89873417682077 84.5196850393724 L 161.6582278477175 84.07874015748305 L 165.41772151861423 76.28871391076109 L 169.17721518951097 76.95013123359679 L 172.93670886040772 82.75590551181165 L 176.69620253130444 108.18372703412113 L 180.45569620220118 99.58530183727038 L 184.21518987309793 84.29921259842605 L 187.97468354399464 74.15748031496088 L 191.7341772148914 61.14960629921323 L 195.49367088578813 72.17322834645711 L 199.25316455668488 58.72440944882011 L 203.0126582275816 48.362204724411924 L 206.77215189847834 36.30971128609289 L 210.5316455693751 34.03149606299287 L 214.2911392402718 28.00524934383502 L 218.05063291116855 10.000000000001336 L 221.8101265820653 14.923884514437475 L 225.569620252962 32.92913385827116 L 229.32911392385876 35.20734908136782 L 233.0886075947555 25.874015748034807 L 236.84810126565222 13.601049868769422 L 240.60759493654896 22.346456692916632 L 244.3670886074457 17.128608923887583 L 248.12658227834243 29.622047244095995 L 251.88607594923917 31.312335958006855 L 255.64556962013592 35.06036745407138 L 259.40506329103266 33.59055118110352 L 263.1645569619294 45.422572178479555 L 266.9240506328261 37.26509186351815 L 270.68354430372284 38.734908136486 L 274.4430379746196 28.00524934383502 L 278.20253164551633 32.41469816273191 L 281.9620253164131 31.238845144360297 L 285.7215189873098 42.40944881890063 L 289.48101265820657 73.27559055118218 L 293.24050632910325 87.60629921260121 L 297 80.77165354330788 L 307 80.77165354330788" stroke-linejoin="round" visibility="visible" stroke="rgba(192,192,192,0.0001)" stroke-width="21" zIndex="2" class=" highcharts-tracker" style=""></path></g><g class="highcharts-markers highcharts-tracker" visibility="visible" zIndex="0.1" transform="translate(1,0) scale(1 1)" style="" clip-path="none"></g><g class="highcharts-series" visibility="visible" zIndex="0.1" transform="translate(1,0) scale(1 1)" clip-path="url(#highcharts-1)"></g><g class="highcharts-markers highcharts-tracker" visibility="visible" zIndex="0.1" transform="translate(1,0) scale(1 1)" style="" clip-path="none"></g><g class="highcharts-series" visibility="visible" zIndex="0.1" transform="translate(1,0) scale(1 1)" clip-path="url(#highcharts-1)"></g><g class="highcharts-markers highcharts-tracker" visibility="visible" zIndex="0.1" transform="translate(1,0) scale(1 1)" style="" clip-path="none"></g></g><path fill="none" d="M 1 81.5 L 298 81.5" stroke="#C0C0C0" stroke-width="1" stroke-dasharray="none" zIndex="4"></path><text x="301" text-anchor="undefined" zIndex="4" transform="translate(0,0)" style="font-size:9px;font-family:Arial, sans-serif;color:#fff;fill:#fff;" y="85" visibility="visible">2,384.42</text><g class="highcharts-axis-labels highcharts-xaxis-labels" zIndex="7"><text x="23.306329114211877" text-anchor="start" style="color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="135" opacity="1">07/12</text>
													<text x="158.89873417682077" text-anchor="start" style="color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="135" opacity="1">12:00</text><text x="249.12658227834243" text-anchor="start" style="color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="135" opacity="1">14:00</text></g><g class="highcharts-axis-labels highcharts-yaxis-labels" zIndex="7"><text x="295" text-anchor="end" style="width:78px;color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="113.25459317585373" opacity="1">2,380.00</text><text x="295" text-anchor="end" style="width:78px;color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="39.76377952756117" opacity="1">2,390.00</text><text x="295" text-anchor="end" style="width:78px;color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="150" opacity="1">2,375.00</text><text x="295" text-anchor="end" style="width:78px;color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="76.50918635170744" opacity="1">2,385.00</text><text x="0" text-anchor="end" style="width:78px;color:#A0A0A0;cursor:default;font-size:11px;font-family:Arial, sans-serif;fill:#A0A0A0;" y="-9999">2,395.00</text></g><g class="highcharts-tooltip" zIndex="8" style="cursor:default;padding:0;white-space:nowrap;pointer-events:none;" transform="translate(158,-9999)" opacity="0" visibility="visible"><path fill="none" d="M 1.5 0.5 L 88.5 0.5 C 89.5 0.5 89.5 0.5 89.5 1.5 L 89.5 34.5 C 89.5 35.5 89.5 35.5 88.5 35.5 L 1.5 35.5 C 0.5 35.5 0.5 35.5 0.5 34.5 L 0.5 1.5 C 0.5 0.5 0.5 0.5 1.5 0.5" isShadow="true" stroke="black" stroke-opacity="0.049999999999999996" stroke-width="5" transform="translate(1, 1)" width="89" height="35"></path><path fill="none" d="M 1.5 0.5 L 88.5 0.5 C 89.5 0.5 89.5 0.5 89.5 1.5 L 89.5 34.5 C 89.5 35.5 89.5 35.5 88.5 35.5 L 1.5 35.5 C 0.5 35.5 0.5 35.5 0.5 34.5 L 0.5 1.5 C 0.5 0.5 0.5 0.5 1.5 0.5" isShadow="true" stroke="black" stroke-opacity="0.09999999999999999" stroke-width="3" transform="translate(1, 1)" width="89" height="35"></path><path fill="none" d="M 1.5 0.5 L 88.5 0.5 C 89.5 0.5 89.5 0.5 89.5 1.5 L 89.5 34.5 C 89.5 35.5 89.5 35.5 88.5 35.5 L 1.5 35.5 C 0.5 35.5 0.5 35.5 0.5 34.5 L 0.5 1.5 C 0.5 0.5 0.5 0.5 1.5 0.5" isShadow="true" stroke="black" stroke-opacity="0.15" stroke-width="1" transform="translate(1, 1)" width="89" height="35"></path><path fill="rgba(249, 249, 249, .85)" d="M 1.5 0.5 L 88.5 0.5 C 89.5 0.5 89.5 0.5 89.5 1.5 L 89.5 34.5 C 89.5 35.5 89.5 35.5 88.5 35.5 L 1.5 35.5 C 0.5 35.5 0.5 35.5 0.5 34.5 L 0.5 1.5 C 0.5 0.5 0.5 0.5 1.5 0.5" stroke="rgb(0, 96, 152)" stroke-width="1"></path><text x="5" zIndex="1" style="font-size:10px;font-family:Arial, sans-serif;color:#333333;fill:#333333;" y="16"><tspan style="font-weight:bold">2390.34</tspan><tspan x="5" dy="14">07/12/2022 14:25</tspan></text></g></svg></div></div><div id="quotesBoxChartLoading" class="loading-responsive medium-circle" style="display: none;"></div>
				
									
													<div class="aside_area aside_popular"> 
														<h3 class="h_popular"><span>인기 검색 종목</span></h3> 
														<table class="tbl_home">
														 <colgroup> 
														  <col> 
														  <col width="60"> 
														  <col width="115"> 
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
													
					</div>

					<div id="chart-area">
						
					</div>
				</article>
			</section>
			
		</main>
		<%@ include file="/WEB-INF/views/trading/inc/footer.jsp" %>
	</div>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
	<script src="/js/common.js"></script>
</body>
</html>