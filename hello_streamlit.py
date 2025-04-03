import re

st = """<html xmlns="http://www.w3.org/1999/xhtml" lang="ko" xml:lang="ko" class="pweb js flexbox canvas canvastext webgl no-touch geolocation postmessage no-websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage webworkers no-applicationcache svg inlinesvg smil svgclippaths linux chrome etc" style=""><head> <title>이름분석 &gt; 이름어때 &gt; 데이터 놀이터 &gt; 미소짓는 데이터생활 &gt; NICE지키미</title> <meta http-equiv="Content-Type" content="text/html;charset=euc-kr"> <meta charset="euc-kr"> <meta http-equiv="Expires" content="0"> <meta http-equiv="Pragma" content="no-cache"> <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate"> <meta name="title" content="나이스지키미"> <meta name="keywords" content="신용조회, 신용정보, 신용등급, 신용관리, 신용등급조회, 신용등급확인, 신용정보조회, 신용등급무료조회, 무료신용조회, 무료신용등급조회, 나이스신용지키미, 나이스지키미 무료, 내신용등급확인, 나이스신용정보, 신용정보조회, 연체정보, 개인채무조회, 전국민무료신용조회, 신용변동, 개인정보보호, 명의보호, 대출, 카드, 나이스 신용조회, 크레딧뱅크, 나이스지키미, 마이크레딧, 마이크래딧, 나이스 지키미, 나이스, 나이스지킴이, NICE지키미, 신용정보조회사이트, 등급하락 없는 조회, 신용상승 컨설팅, 신용등급 변동예측, 신용등급 예측, 신용등급 시뮬레이터, 나이스 무료신용조회, 나이스지키미 신용등급, 나이스지키미 무료, nice지키미, 나이스 신용등급, 나이스지키미 신용등급계산기, 나이스지키미신용등급, 신용등급 조회, 나이스지키미신용등급계산기, 나이스 회원가입, 나이스 로그인, 나이스크레딧, 소상공인대출등급, 소상공인대출신용, 소상공인대출신용등급, 소상공인사업자대출신용등급, 소상공인시장진흥공단대출등급, 소상공인시장진흥공단대출신용, 소상공인시장진흥공단대출신용등급, 소상공인신용, 소상공인신용등급, 소상공인신용등급조회, 소상공인신용보증재단대출등급, 소상공인신용점수, 소상공인신용정보, 소상공인신용정보조회, 소상공인신용조회, 소상공인신용평가, 소상공인신용평점, 소상공인진흥공단대출등급, 소상공인진흥공단대출신용, 소상공인진흥공단대출신용등급, 신용보증기금대출등급, 신용보증기금대출신용, 신용보증기금대출신용등급, 자영업대출등급, 자영업대출신용, 자영업대출신용등급, 자영업신용, 자영업신용등급, 자영업신용등급조회, 자영업신용점수, 자영업신용정보, 자영업신용정보조회, 자영업신용조회, 자영업신용평가, 자영업신용평점, 자영업자대출등급, 자영업자대출신용, 자영업자대출신용등급, 자영업자신용, 자영업자신용등급, 자영업자신용등급조회, 자영업자신용점수, 자영업자신용정보, 자영업자신용정보조회, 자영업자신용조회, 자영업자신용평가, 자영업자신용평점"> <meta name="description" content="1위 신용평가기관, 신용점수 올라가는 나이스한 신용습관"> <meta property="og:image" content="https://img.credit.co.kr/resource/img/zkm/common/zikimi_meta.jpg"> <meta property="og:title" content="나이스지키미"> <meta property="og:description" content="1위 신용평가기관, 신용점수 올라가는 나이스한 신용습관"> <meta property="og:type" content="website"> <meta property="og:url" content="https://www.credit.co.kr/ib20/mnu/BZWMNLGNM20"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- 페이지템플릿 리소스 --> <link rel="shortcut icon" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/favicon.ico"> <link rel="icon" type="image/png" sizes="16x16" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/favicon-16x16.png"> <link rel="icon" type="image/png" sizes="32x32" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/favicon-32x32.png"> <link rel="icon" type="image/png" sizes="48x48" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/favicon-48x48.png"> <link rel="icon" type="image/png" sizes="196x196" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/favicon-196x196.png"> <link rel="apple-touch-icon" sizes="57x57" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/apple-touch-icon-57x57.png"> <link rel="apple-touch-icon" sizes="72x72" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/apple-touch-icon-72x72.png"> <link rel="apple-touch-icon" sizes="114x114" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/apple-touch-icon-114x114.png"> <link rel="apple-touch-icon" sizes="120x120" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/apple-touch-icon-120x120.png"> <link rel="apple-touch-icon" sizes="144x144" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/apple-touch-icon-144x144.png"> <link rel="apple-touch-icon" sizes="152x152" href="https://img.credit.co.kr/resource/img/zkm/common/favicon/apple-touch-icon-152x152.png"> <meta name="msapplication-TileImage" content="https://img.credit.co.kr/resource/img/zkm/common/favicon/apple-touch-icon-144x144.png"> <script async="" src="//fs.bizspring.net/fs4/logger.v4.1.js"></script><script async="" src="//fs.bizspring.net/fs4/bstrk.1.js"></script><script type="text/javascript" src="/cmn/js/include/zkm/rzm/package.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/lib/jquery-1.11.3.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/lib/jquery-ui.min.js?v=2202503111626"></script> <script type="text/javascript"> // #5.1# var FAKE_FLAG = 'N'; SYSTEM_TIME = '1743697668164'; IMG_ROOT = 'https://img.credit.co.kr/resource'; SECURE_TYPE = ""; USER_ID = "64493b4bcf7e027c147863d8a0f789ff4ec8b62b9ad32a07ced071f7fdb64ab5"; HASH_USER_ID = "c84cf87aef4b89878bfe9b6799dfbb749e5e2117b465c153f07afa282ff3ea87"; LOGIN_YN = "Y"; MEDIA_TYPE = "P"; DEF_ERR_PGE = "BZWCMMERR01"; LOGOUT_MENU_ID = "BZWSGMMLU20"; MAIN_MENU_ID = "BZWMAN00001"; CURRENT_SITE_ID = "SIT00002"; CURRENT_MENU_ID = "BZWMNLGNM20"; MENU_PREFIX_3 = "BZW"; SERVICE_MODE = ''; LOCAL_YN = 'N'; PREFIX_URL = ''; LOGOUT_SESSION_TIME = parseInt('10'); LOGOUT_USER_TIME = parseInt('10'); if (LOGOUT_SESSION_TIME > LOGOUT_USER_TIME) { LOGOUT_SESSION_TIME = LOGOUT_USER_TIME; } /** * 페이지 이동 타입을 반환한다. * @returns */ function getNavigationType() { var result; var p; if (window.performance && window.performance.navigation) { result = window.performance.navigation; if (result == 255) result = 4; //기타 } if (window.performance && window.performance.getEntriesByType("navigation")) { try { p = window.performance.getEntriesByType("navigation")[0].type; if (p == "navigate") result = 0; //일반적인 URL이동 if (p == "reload") result = 1; //새로고침 if (p == "back_forward") result = 2; //앞/뒤로가기 if (p == "prerender") result = 0; } catch(e) { p = 0; } } return result; } // #5.2# if (localStorage.getItem("ZKM_SYSTEM_TIME") > SYSTEM_TIME) { location.reload(); } else { localStorage.setItem("ZKM_SYSTEM_TIME", SYSTEM_TIME); } // #5.3# if (MEDIA_TYPE == "P") { $("html").addClass("pweb"); } else { $("html").addClass("mobile"); } </script> <script type="text/javascript" src="/cmn/js/include/lib/jquery.selectbox.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/lib/modernizr-2.6.2.min.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/lib/jquery.alphanumeric.plus.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/lib/jquery.form.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/lib/jquery.urldecoder.min.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/lib/json2.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/util/utils.js?v=2202503111626"></script> <script type="text/javascript"> if (SYSTEM_TIME != '') { JUtilDate.initSystemTime(SYSTEM_TIME); } //SIT00003(제휴서비스), SIT00006(제휴서비스모바일) if (CURRENT_SITE_ID != "SIT00003" && CURRENT_SITE_ID != "SIT00006" ) { if ((["SIT00001", "SIT00002", "SIT00004", "SIT00005", "SIT00014", "SIT00017", "SIT00018"].indexOf("SIT00002") >= 0) && parent.name != 'top'){ if (MEDIA_TYPE == 'M') { if (opener == null) { window.name = "top"; } } else { if ("CMNCRT00007" != "BZWMNLGNM20") { window.name = "top"; } } } } </script> <script type="text/javascript" src="/resource/js/handlebars.min-v4.7.6.js"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/lib/base64.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/lib/in-view.min.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/lib/swiper.min.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/lib/odometer.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/lib/jquery.ui.monthpicker.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_jquery.js?v=2202503111626"></script> <!-- <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_effect.js?v=2202503111626"></script> --> <!-- <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_block.js?v=2202503111626"></script> --> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_pop.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_message.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_logout_timer.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_validation.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_calendar.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_e2e.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ext/ext_keypad.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/common.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/util/handlebarUtils.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/util/bizutils.js?v=2202503111626"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/util/zkmUtils.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/common.js?v=2202503111626"></script> <!-- <script type="text/javascript" src="/resource/js/zkm/rzm/ui.common.js?v=2202503111626"></script> --> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/ui.common.js?v=2202503111626"></script> <link rel="stylesheet" href="https://img.credit.co.kr/resource/css/zkm/rzm/swiper.min.css?v=2202503111626"> <link rel="stylesheet" href="https://img.credit.co.kr/resource/css/zkm/rzm/odometer-theme-default.css?v=2202503111626"> <link rel="stylesheet" href="https://img.credit.co.kr/resource/css/zkm/rzm/common.css?v=2202503111626"> <link rel="stylesheet" href="/resource/css/zkm/rzm/font.css?v=2202503111626"> <style type="text/css"> /* 템플릿용 태그 숨김 처리 */ template {display:none;} xmp[render-target] {display:none;} /* full 레이어 팝업 호출 시 스크롤 동작 하도록 스타일 지정 */ .uiModal .modalWrap>form {height:100%;} .stackedBar .emptyBar {width:100%; background-color:#f0f0f0;} .headerMob .btnPrev, .headerMob .btnGnb {display:none;} </style> <script type="text/javascript" src="/resource/product/astx/astx2/astx2.min.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/product/astx/astx2/astx2_jq.min.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/product/astx/astx2/astx2_custom.js?v=2202503111626"></script> <script src="/resource/product/kings/kdfense_object.js?v=2202503111626"></script> <link rel="stylesheet" type="text/css" href="/resource/product/transkey/transkey.css?v=2202503111626"> <script type="text/javascript" src="/resource/product/transkey/transkey.js?v=2202503111626"></script><script type="text/javascript" src="/resource/product/transkey/rsa_oaep_files/rsa_oaep-min.js"></script><script type="text/javascript" src="/resource/product/transkey/jsbn/jsbn-min.js"></script><script type="text/javascript" src="/resource/product/transkey/TranskeyLibPack_op.js"></script><script type="text/javascript" src="/transkeyServlet?op=getToken&amp;1743697668417"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/transkey_common.js?v=2202503111626"></script> <script type="text/javascript" src="/resource/product/wiselog/makePCookie.js?v=2202503111626"></script> <script type="text/javascript" charset="UTF-8" src="//t1.daumcdn.net/adfit/static/kp.js"></script> <script type="text/javascript"> window["kakaoPixel"] && kakaoPixel('6379261639961035839').pageView(); </script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/util/lodash.min.js?v=2202503111626"></script><!-- 메뉴 리소스 --> <script type="text/javascript" src="/resource/product/fusioncharts.v318/js/fusioncharts.js"></script> <script type="text/javascript" src="/resource/product/fusioncharts.v318/js/themes/fusioncharts.theme.fint.js"></script> <script type="text/javascript" src="/resource/js/zkm/rzm/fusioncharts.theme.zkm.rzm.js"></script> <script type="text/javascript" src="/cmn/js/include/zkm/rzm/util/chartUtils.js"></script><script charset="utf-8" src="/resource/product/fusioncharts.v318/js/fusioncharts.charts.js"></script></head> <body> <div id="wrap"> <div id="accessibilityMenu"> <div id="CMNZKMTMP00003VM"> <div id="skipNavi"> <a href="#content">본문내용 바로가기</a> </div> </div> </div><div id="header"> <div id="CMNZKMTMP00001VM"> <script type="text/javascript">
$(document).ready(function() {
	// 뒤로 가기 버튼 클릭
	$(".btnPrev").on("click", function(e) {
		goBack();
	});

	//검색어 입력창 enter 키 이벤트 지정
	$(".menuSearh .inputSrh").on("keydown", function(e) {
		if (e.keyCode == 13) {
			openMenuSearchPopup($(this).parent().find(".btnSrh"));
		}
	});


	// #6#
	var recentlyMenuList = JUtilObject.recentlyMenu.getList().slice(0, 3);
	JUtilObject.renderPage(recentlyMenuList, ".recentUse");





var chgPop = 'Y';




	if("Y"==chgPop){
		openMyDataAgreePop();
	}












var idPopYn = 'N';



		if ("Y" == idPopYn) {
			addReadyOpenPopup("joinInfoUpd");
		}


	ExtValidation.inputFilter($("#form_headerView"));

});

//마이데이터 가입동의 팝업 호출(필요시 업무 화면에서 함수 호출)
function openMyDataAgreePop(forced, callback) {


}


//커스텁 팝업 호출(필요시 업무 화면에서 함수 호출) //필요시 메뉴 부분 추가 수정
function openCustAgreePop(forced, widget, popId, pviewType, paramYn ,callback) {



	callback = callback || function(rtnVal) {
		if (rtnVal == "Y") {
			reload();
		}
	};

	if(!localStorage[popId+"PopDate"] || localStorage[popId+"PopDate"] < JUtilDate.getToday()){
		if("Y" == (paramYn || 'Y')){
			if (forced === true) {	//화면 로딩시 호출이 아니면 forced를 true로 넘긴다.
				var mdpopForm = JUtilForm.createForm(widget+"Form");
				appendHidden(mdpopForm, "menuId", "BZWMNLGNM20");
				ExtLayerPop.load(mdpopForm, 'BZWMNLGNM20', widget, null, null, {viewType : pviewType, callback : callback});
			} else {
				addReadyCustOpenPopup(popId, function() {
					var mdpopForm = JUtilForm.createForm(widget+"Form");
					appendHidden(mdpopForm, "menuId", "BZWMNLGNM20");
					ExtLayerPop.load(mdpopForm, 'BZWMNLGNM20',widget, null, null, {viewType : pviewType, callback : callback});
				});
			}
		}
	}


}

function openBigEyePop(linkUrl) {
	var  contextUrl = "https://www.credit.co.kr";
	contextUrl += '/ib20/mnu/RZMCMNURL02?param_r1='+linkUrl;
	if ("P" == "A") {
		sendToApp("open_inappbrowser", {"url" : "" + encodeURI(contextUrl) + ""});
	} else if ("P" == "M"){
		window.open(linkUrl, "_blank");	
	} else{
		window.open(linkUrl, "_blank");
	}
}

function openExtUrl(url) {
	if ("P" == "A") {
		sendToApp("open_inappbrowser", {"url" : "" + encodeURI(url) + ""});
	} else if ("P" == "M"){
		window.open(url, "_blank");	
	} else{
		window.open(url, "_blank");
	}
	                            		전국에<br><strong>1,343</strong>명

}"""

pattern = r'전국에<br><strong>[\d,]+</strong>명'
match = re.findall(pattern, st)
test = re.findall(r'[\d,]+', match[0])