<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<script type="text/javascript" src="check.js"></script>
<jsp:include page="header.jsp"/>

<section style="position:fixed; top:70px; left:0px; width:100%; height:100%; background-color:lightgray">
<h2 style="text-align:center"> 좌석예약 조회 </h2>
<form method="post" action="l_action.jsp" name="frm2" style="display:flex; align-items:center; justify-content:center">
<table border="1">
<tr>
	<td>사원번호를 입력하시오.</td>
	<td><input type="text" name="empno"></td>
</tr>
<tr style="text-align:center">
	<td colspan="2">
	<input type="button" value="좌석예약조회" onclick="search()">
	<input type="button" value="홈으로" onclick="home()">
	</td>
</tr>
</table>
</form>
</section>
<jsp:include page="footer.jsp"/>
</body>
</html>