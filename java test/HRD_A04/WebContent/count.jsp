<%@ page import="DBPKG.Util" %>
<%@ page import="java.sql.*" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<jsp:include page="header.jsp"/>

<section style="position:fixed; top:70px; left:0px; width:100%; height:100%; background-color:lightgray">
<h2 style="text-align:center"> 좌석예약 조회 </h2>
<form  style="display:flex; align-items:center; justify-content:center">
<table border="1">
	<tr>
		<td>사원번호</td>
		<td>이름</td>
		<td>부서명</td>
		<td>근무일수</td>
	</tr>
<%
	request.setCharacterEncoding("utf-8");
	try{
		Connection conn = Util.getConnection();
		String sql = "select em.empno, empname, deptcode, count(resvno) from tbl_emp_202108 em, tbl_resv_202108 re where em.empno=re.empno group by em.empno, empname, deptcode order by deptcode";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		ResultSet rs = pstmt.executeQuery();
		while(rs.next()){
			String deptcode = rs.getString(3);
			if(deptcode.equals("10")) deptcode = "영업팀";
			else if(deptcode.equals("20")) deptcode = "총무팀";
			else if(deptcode.equals("30")) deptcode = "구매팀";
%>
	<tr>
		<td><%=rs.getString(1) %></td>
		<td><%=rs.getString(2) %></td>
		<td><%=deptcode %></td>
		<td><%=rs.getString(4) %></td>
	</tr>
<%
		}
	}catch(Exception e){
		e.printStackTrace();
	}
%>
</table>
</form>
</section>
<jsp:include page="footer.jsp"/>
</body>
</html>