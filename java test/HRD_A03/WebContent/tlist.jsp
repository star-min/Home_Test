<%@page import="java.text.DecimalFormat"%>
<%@ include file="db.jsp" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>강사조회</title>
</head>
<body>
<form action="" style="display: flex; align-items:center; justify-content:center; text-align: center;">
<table border="1">
	<tr>
		<td style="width:150px">강사코드</td>
		<td style="width:150px">강사명</td>
		<td style="width:150px">강의명</td>
		<td style="width:150px">수강료</td>
		<td style="width:150px">강사자격취득일</td>
	</tr>
	<%
	request.setCharacterEncoding("UTF-8");
	
	try{
		String sql = "select * from TBL_TEACHER_202201 order by teacher_code";
		pstmt = con.prepareStatement(sql);
		rs = pstmt.executeQuery();
		while(rs.next()){
			int class_price = rs.getInt(4);
			DecimalFormat transFormat = new DecimalFormat("￦ ###,###,###");
			String price = transFormat.format(class_price);
			
			String teach_resist_date = rs.getString(5);
			String date = teach_resist_date.substring(0,4)+"년"+teach_resist_date.substring(4,6)+"월"+teach_resist_date.substring(6,8)+"일";
		%>
		<tr>
			<td> <%=rs.getString(1) %> </td>
			<td> <%=rs.getString(2) %> </td>
			<td> <%=rs.getString(3) %> </td>
			<td> <%=price %> </td>
			<td> <%=date %> </td>
		</tr>
		<%
		}
	}
	catch(Exception e){
		e.printStackTrace();
	}
	%>
</table>
</form>
</body>
</html>