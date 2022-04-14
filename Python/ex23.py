# 리스트(순서자료구조)의 추가, 삭제, 수정, 삽입
lst = ["심", "박", "이", "김", "조", "여"]
print("추가 전 : ", lst)
lst.append("고")
print("추가 후 : ", lst)

print("제거 전 : ", lst)
lst.remove("조")
print("제거 후 : ", lst)

print("변경 전 : ", lst)
lst[0] = "전"
print("변경 후 : ", lst)

print("삽입 전 : ", lst)
lst.insert(2, "옹")
print("삽입 후 : ", lst)

# 리스트는 가공을 하게 되면, 항상 순서를 유지한다.