# 자료 구조 : 자료가 저장되는 방식 또는 원리
# 순서형 : 스택(LIFO-최근문서), 큐(FIFO-프로세스) ,데크(스택+큐)
# 비순서형 : 그래프, 트리
# 열거형 : list, set, tuple, dict
# 리스트 : 순서 자료 구조
# 리스트 선언시 열거형변수명 = [요소1,요소2,요소3]
lst = ["김", "이", "박", "최", "정", "오"] # 입력
print(lst)
print(lst[2])
print("lst의 타입 : ", type(lst))
#문자열은 모두 순차 자료
object = 1004
print(type(object))
str_data = str(object)
print(type(str_data))
str_data2 = "김성민" + str(object)
print(str_data2)

print(str_data2[4])
print(str_data2[:2])