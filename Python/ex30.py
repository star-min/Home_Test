# dict(dictionary) : 사전형
# 사전과 같이 "단어 : 뜻" 으로 전개되는 자료형으로 비순서형, 중복된
# 키를 허용하지 않으며, 키 : 값 처럼 키(항목이름)ㅘ 그에 해당하는 순서 쌍으로
# 구성되며, {}로 선언함
man = {"name":"김성민", "age":27, "height": 175, "weight":70}
print("자료형 종류 : ",type(man), "데이터 : ", man)

# 열거형 자료 - 순서형  : ,list, tuple
# 열거형 자료 - 비순서형 : set, dict
print("man 의 이름 : ", man['name'])   # 특정 항목의 출력
man['name'] = "이동주"
print("man 의 이름 : ", man['name'])
woman = dict(name = '이동은', age = 20)    # 선언2
print(woman['name'],"의 나이 : ", woman['age'])
# del man['weight']       # 특정 항목(키) 삭제
# print(man['weight'])    # 해당 키(항목)이 삭제 되었으므로 error
man['from'] = "kor"           # 특정 항목(키)와 그 값의 추가
print(man)