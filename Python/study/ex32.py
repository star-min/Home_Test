# 객체나 자료형의 복제
kims = ["김성민", "이순신", "강감찬", "혁거세"]
lees = ["세종대왕", "광개토대왕", "김유신", "율곡 이이"]
names = kims        # 데이터가 있는 곳의 주소를 전달
print("kims의 메모리 주소 : ", id(kims), "데이터 : ", kims)
print("names의 메모리 주소 : ", id(names), "데이터 : ", names)
names[3] = "알렉산더대왕"         # 같은 곳을 가리키고 있으므로 사본을 바꾸면, 원본도 변경됨
print(kims)
print(names)

import copy
lst = copy.deepcopy(kims)           # 깊은 복제 : 데이터는 같으나 다른 장소에 복제
print(kims, "의 주소 : ", id(kims))
print(lst, "의 주소 : ", id(lst))
lst[3] = "장영실"
print(lst)
print(kims)