<%@page import="java.text.DecimalFormat"%>
<%@page import="java.beans.DesignMode"%>
<%@ include file="db.jsp" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>회원목록</title>
</head>
<body>


<section style="">
<h2>회원정보조회</h2>
<form style="">
	<table>
		<tr>
			<td style="width: 150px">수강일</td>
			<td style="width: 150px">회원정보</td>
			<td style="width: 150px">회원명</td>
			<td style="width: 150px">강의명</td>
			<td style="width: 150px">강의장소</td>
			<td style="width: 150px">수강료</td>
			<td style="width: 150px">등급</td>
		</tr>
		
<%
request.setCharacterEncoding("UTF-8");
try{
	String sql = "select resist_month, cl.c_no, c_name, class_name, class_area, tuition, grade " +
				 "from tbl_teacher_202201 te, tbl_member_202201 me, tbl_class_202201 cl " +
				 "where te.teacher_code=cl.teacher_code and me.c_no=cl.c_no order by c_no";
	pstmt = con.prepareStatement(sql);
	rs = pstmt.executeQuery();
	while(rs.next()){
		String resist_ment = rs.getString(1);
		String month = resist_ment.substring(0,4)+"년"+resist_ment.substring(4,6)+"월";
		int tuition = rs.getInt(6);
		DecimalFormat transformat = new DecimalFormat("￦ ###,###,###");
		String price = transformat.format(tuition);
		%>
	
		<tr>
			<td><%= month %></td>
			<td><%= rs.getString(2) %></td>
			<td><%= rs.getString(3) %></td>
			<td><%= rs.getString(4) %></td>
			<td><%= rs.getString(5) %></td>
			<td><%= price %></td>
			<td><%= rs.getString(7) %></td>
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
</section>


</body>
</html>