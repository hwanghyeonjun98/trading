📦src<br/>
 ┣ 📂main<br/>
 ┃ ┣ 📂java<br/>
 ┃ ┃ ┗ 📂com<br/>
 ┃ ┃ ┃ ┗ 📂big15<br/>
 ┃ ┃ ┃ ┃ ┗ 📂tradingweb<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂controller // 컨트롤러<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜Error.java // 404, 500 erroe 컨트롤러<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜TradingController.java // 트레이딩 컨트롤러<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜TradingRestController.java // rest api 컨트롤러<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂dto<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜InvestingDto.java // investing data DTO<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂mapper<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜InvestingMapper.java // mybatis mapper<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂model<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂service<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜Service.java // 서비스<br/>
 ┃ ┣ 📂resources<br/>
 ┃ ┃ ┣ 📂mybatis<br/>
 ┃ ┃ ┃ ┗ 📂mapper<br/>
 ┃ ┃ ┃ ┃ ┗ 📜InvestingMapper.xml // sql mapper<br/>
 ┃ ┃ ┣ 📂static<br/>
 ┃ ┃ ┃ ┣ 📂css<br/>
 ┃ ┃ ┃ ┃ ┣ 📜common.css // 공통 css<br/>
 ┃ ┃ ┃ ┃ ┣ 📜dataview.css // 데이터 보기 페이지 css<br/>
 ┃ ┃ ┃ ┃ ┣ 📜error_common.css // error css<br/>
 ┃ ┃ ┃ ┃ ┣ 📜index.css // 메인 페이지 css<br/>
 ┃ ┃ ┃ ┃ ┗ 📜reset.css // css 초기화<br/>
 ┃ ┃ ┃ ┣ 📂img<br/>
 ┃ ┃ ┃ ┃ ┣ 📂browser_icon // 브라우저 아이콘<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📜04.05 symbol_whalebook_color_dark.svg // 웨일 아이콘 <br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Fx_Browser.svg // 파이어폭스 아이콘<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Google_Chrome.png // 크롬 아이콘<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Microsoft_Edge.png // 엣지 아이콘<br/>
 ┃ ┃ ┃ ┃ ┃ ┗ 📜Whale_icon.svg // 웨일2 아이콘<br/>
 ┃ ┃ ┃ ┣ 📂js<br/>
 ┃ ┃ ┃ ┃ ┣ 📜chart_js.js // 차트 설정<br/>
 ┃ ┃ ┃ ┃ ┣ 📜common.js // 공통 기능<br/>
 ┃ ┃ ┃ ┃ ┣ 📜data_ajax.js // investing data 비동기 통신<br/>
 ┃ ┃ ┃ ┃ ┣ 📜data_list.js // 메뉴 생성<br/>
 ┃ ┃ ┃ ┃ ┣ 📜error_page.js // 에러시 이전 페이지 이동 스크립트<br/>
 ┃ ┃ ┃ ┃ ┗ 📜table-sort.js // 테이블 정렬 라이브러리<br/>
 ┃ ┃ ┗ 📜application.properties<br/>
 ┃ ┣ 📂webapp<br/>
 ┃ ┃ ┗ 📂WEB-INF<br/>
 ┃ ┃ ┃ ┗ 📂views<br/>
 ┃ ┃ ┃ ┃ ┗ 📂trading<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂dataview // 데이터 조회 관련<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜dataview.jsp<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂errors // error 관련<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜404.jsp<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜500.jsp<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜browser_info.jsp // 브라우저 체크 후 IE에서만 나옴<br/>
 ┃ ┃ ┃ ┃ ┃ ┣ 📂inc<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜defualt_css.jsp // 기본으로 적용할 CSS 모음<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜footer.jsp // footer<br/>
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜header.jsp // header <br/>
 ┃ ┃ ┃ ┃ ┃ ┗ 📜index.jsp // 메인페이지<br/>
