import datetime
from datetime import date, time
print("오늘 날짜 : ", datetime.datetime.today())
print("현재 : ", datetime.datetime.now())
today1 = datetime.datetime.today()
today2 = datetime.datetime.now()
time1 = today1.time()
date1 = today1.date()
print("현재 시간 : ", time1)
print("현재 날짜 : ", date1)
print("현재 년도 : ", today1.year)
print("현재 월 : ", today1.month)
print("현재 일 : ", today1.day)
print("현재 시 : ", today1.hour)
print("현재 분 : ", today1.minute)
print("현재 초 : ", today1.second)
print("오늘의 요일 번호 : ", today1.weekday())
lst = ["월", "화", "수", "목", "금", "토", "일"]
print("오늘의 요일 : ",lst[today1.weekday()])
birth = date(1995,5,22)
print("생년월일 : ", birth)
print("살아온 일 수 : ", date1-birth)
birth2 = "19950522"
from datetime import datetime
b = datetime.strptime(birth2, "%Y%m%d")
lifeday = today1 - b
print(lifeday)
