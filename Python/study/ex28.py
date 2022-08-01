# 비순서형 자료구조 set
# set 의 특징 : 중복을 허용하지 않음, 순서 유지가 되지 않음
# {} 중괄호 사용, 인덱스가 없다(순서가 없어서), 집합과 그 특성이 같다.
stl = { 80, 85, 75, 70, 80, 85}
print(type(stl), len(stl), stl)
st2 = { 65, 70, 75, 80}
# st3 = {} - 공집합은 연산이 되지않음
st3 = st2.union(stl)                # union 은 합집합
st4 = st2.intersection(stl)         # intersection 은 교집합
st5 = stl.difference(st2)           # difference 는 차집합
st6 = st2.difference(stl)
print("합집합 : ", st3)
print("교집합 : ", st4)
print("stl - st2 = stl에는 있고, st2에는 없는 원소", st5)
print("st2 - st1 = st2에는 있고, stl에는 없는 원소", st6)

# 관련 매서드 : 원소 추가(add), 원소 삭제(discard)
stl.add(50)
print("stl에 50 원소 추가 : ", stl)
stl.discard(70)
print("stl에 70 원소 삭제 : ", stl)