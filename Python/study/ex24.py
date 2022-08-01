# 리스트 끼리 연산(결합, 확장, 추가, 두 배 확장)
lst1 = ["정", "오", "박", "최"]
lst2 = ["김", "이", "전", "연"]

# 리스트의 결합
lst3 = lst1 + lst2
print("결합 후 : ", lst3)

# 리스트의 확장
print("확장 전 : ", lst1)
lst1.extend(lst2)
print("확장 후 : ", lst1)

lst4 = ["정", "오", "박", "최"]
lst5 = ["김", "이", "전", "연"]
# 리스트의 추가
print("추가 전 : ", lst4)
lst4.append(lst5)
print("추가 후 : ", lst4)

# 리스트의 두 배 확장
res = lst5 * 2
print("lst5의 두 배 확장 : ", res)

print("정렬 전 : ", lst1)
lst1.sort()
print("순차 정렬 후 : ", lst1)
lst1.sort(reverse=True)
print("역순 정렬 후 : ", lst1)

import random
lst6 = []
for i in range(1, 10) :
    lst6.append(random.randint(1, 9))
print(lst6)

# 리스트의 검사 : 해당 값이 리스트의 존재 여부를 판단
if 6 in lst6 :
    print("6 이 존재 함")
else :
    print("6이 존재 하지 않음")
