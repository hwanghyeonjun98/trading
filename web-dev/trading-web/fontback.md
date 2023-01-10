# Font End & Back End
## 디렉토리 구조

---
**!!!! 스프링 부트 최초 실행 및 처음 클론 시 nodejs 설치하고**<br>
**<code>/trading/web-dev/trading-web/src/main/resources/static</code> 디렉토리 접근 후**<br>
**터미널에서 <code>npm install</code> 후 스프링 실행**

### 디렉토리 구조

#### Back 단

<pre>
📦java
 ┗ 📂com
 ┃ ┗ 📂big15
 ┃ ┃ ┗ 📂tradingweb
 ┃ ┃ ┃ ┣ 📂controller // 컨트롤러
 ┃ ┃ ┃ ┃ ┣ 📜DeveloperController.java // 개발자 소개
 ┃ ┃ ┃ ┃ ┣ 📜Error.java // 에러 메세지
 ┃ ┃ ┃ ┃ ┣ 📜JoinController.java // 회원가입
 ┃ ┃ ┃ ┃ ┣ 📜JoinRestController.java // 회원가입 API
 ┃ ┃ ┃ ┃ ┣ 📜LoginController.java // 로그인
 ┃ ┃ ┃ ┃ ┣ 📜LoginRestcontroller.java // 로그인 API
 ┃ ┃ ┃ ┃ ┣ 📜LogoutController.java // 로드아웃
 ┃ ┃ ┃ ┃ ┣ 📜TradingController.java // 메인 페이지 
 ┃ ┃ ┃ ┃ ┣ 📜TradingDataController.java // 트레이딩 데이터
 ┃ ┃ ┃ ┃ ┗ 📜TradingRestController.java // 차트, 트레이딩 데이터 API
 ┃ ┃ ┃ ┣ 📂dto
 ┃ ┃ ┃ ┃ ┣ 📜AccountDto.java // 회원 계좌
 ┃ ┃ ┃ ┃ ┣ 📜AccountHistoryDto.java // 트레이딩 내역
 ┃ ┃ ┃ ┃ ┣ 📜AiTradingDto.java // 인공지능 트레이딩 내역
 ┃ ┃ ┃ ┃ ┣ 📜InvestingDto.java // 인베스팅
 ┃ ┃ ┃ ┃ ┣ 📜MarketCapDto.java // 시가총액
 ┃ ┃ ┃ ┃ ┣ 📜NewsDto.java // 뉴스
 ┃ ┃ ┃ ┃ ┗ 📜UserInfoDto.java // 회원 정보
 ┃ ┃ ┃ ┣ 📂mapper
 ┃ ┃ ┃ ┃ ┣ 📜AiTradingMapper.java // 트레이딩 매퍼
 ┃ ┃ ┃ ┃ ┣ 📜IndexdataMapper.java // 메인 페이지 매퍼
 ┃ ┃ ┃ ┃ ┣ 📜InvestingMapper.java // 인페스팅 매퍼
 ┃ ┃ ┃ ┃ ┣ 📜JoinMapper.java // 회원가입 매퍼
 ┃ ┃ ┃ ┃ ┗ 📜LoginMapper.java // 로그인 매퍼
</pre>

### mybais

<pre>
📦mybatis
 ┣ 📂mapper
 ┃ ┣ 📜AiTradingMapper.xml // AI 트레이딩 SQL
 ┃ ┣ 📜IndexdataMapper.xml // 메인 페이지 SQL
 ┃ ┣ 📜InvestingMapper.xml // 인베스팅 SQL
 ┃ ┣ 📜JoinMapper.xml // 회원가입 SQL
 ┃ ┗ 📜LoginMapper.xml // 로그인 SQL
</pre>

#### Front 단

<pre>
📦views
 ┗ 📂trading
 ┃ ┣ 📂dataview
 ┃ ┃ ┗ 📜data.jsp // 데이토 조회
 ┃ ┣ 📂developer
 ┃ ┃ ┗ 📜developer_info.jsp // 개발자 소개 페이지
 ┃ ┣ 📂errors // 에러 페이지
 ┃ ┃ ┣ 📜404.jsp // 404 에러 표시 페이지
 ┃ ┃ ┣ 📜500.jsp // 500 에러 표시 페이지
 ┃ ┃ ┗ 📜browser_info.jsp
 ┃ ┣ 📂inc // 공통 부분
 ┃ ┃ ┣ 📜defualt_css.jsp // favicon 및 공통 CSS 
 ┃ ┃ ┣ 📜footer.jsp // 풋터
 ┃ ┃ ┗ 📜header.jsp // 헤더(메뉴)
 ┃ ┣ 📂login
 ┃ ┃ ┣ 📜join.jsp // 회원가입 페이지
 ┃ ┃ ┗ 📜login.jsp // 로그인 페이지
 ┃ ┗ 📜index.jsp // 메인 페이지
</pre>

<pre>
📦static
 ┣ 📂css
 ┃ ┣ 📜color.css // 컬러 클래스 정의
 ┃ ┣ 📜common.css // 공통 CSS
 ┃ ┣ 📜dataview.css // 데이터 조회 CSS
 ┃ ┣ 📜developer_info.css // 개발자 소개 CSS
 ┃ ┣ 📜error_common.css // 에러 페이지 CSS
 ┃ ┣ 📜index.css // 메인 페이지 CSS
 ┃ ┣ 📜login.css // 로그인 페이지 CSS
 ┃ ┗ 📜reset.css // CSS 리셋 :root 지정
 ┣ 📂img
 ┃ ┣ 📂browser_icon // 브라우저 아이콘
 ┃ ┃ ┣ 📜04.05 symbol_whalebook_color_dark.svg // 웨일
 ┃ ┃ ┣ 📜Fx_Browser.svg // 파이어 폭스
 ┃ ┃ ┣ 📜Google_Chrome.png // 크롬
 ┃ ┃ ┣ 📜Microsoft_Edge.png // 엣지
 ┃ ┃ ┗ 📜Whale_icon.svg // 웨일2
 ┃ ┣ 📂favicon // 브라우저 상단 및 즐겨찾기 아이콘
 ┃ ┃ ┣ 📜android-chrome-192x192.png
 ┃ ┃ ┣ 📜android-chrome-512x512.png
 ┃ ┃ ┣ 📜apple-touch-icon.png
 ┃ ┃ ┣ 📜favicon-16x16.png
 ┃ ┃ ┣ 📜favicon-32x32.png
 ┃ ┃ ┣ 📜favicon.ico
 ┃ ┃ ┗ 📜site.webmanifest
 ┃ ┣ 📂skill_icon // 개발자 소개 페이지에 쓸 언어 라이브러리 로고
 ┃ ┃ ┣ 📜bs.png
 ┃ ┃ ┣ 📜css.png
 ┃ ┃ ┣ 📜html.png
 ┃ ┃ ┣ 📜java.png
 ┃ ┃ ┣ 📜jq.png
 ┃ ┃ ┣ 📜js.png
 ┃ ┃ ┣ 📜mybatis.svg
 ┃ ┃ ┣ 📜mysql.png
 ┃ ┃ ┣ 📜python.svg
 ┃ ┃ ┣ 📜spring.svg
 ┃ ┃ ┗ 📜tensorflow.svg
 ┣ 📂js // 자바스크립트 파일
 ┃ ┣ 📜aiTrading.js // AI 트레이딩 Ajax
 ┃ ┣ 📜chart_js.js // 데이터 페이지 차트 생성
 ┃ ┣ 📜common.js // 공통 기능
 ┃ ┣ 📜data_ajax.js // 데이터 페이지 데이터 Ajax
 ┃ ┣ 📜data_list.js // 데이터 페이지 메뉴 생성 및 애니메이션
 ┃ ┣ 📜error_page.js // 에러 페이지 스크립트
 ┃ ┣ 📜index_ajax.js // 메인 페이지 데이터 Ajax
 ┃ ┣ 📜index_chart.js // 메인 페이지 차트 Ajax
 ┃ ┣ 📜join.js // 회원가입 스크립트 
 ┃ ┣ 📜login_ajax.js // 로그인 Ajax
 ┃ ┗ 📜table-sort.js // 테이블 정렬 라이브러리
</pre>

