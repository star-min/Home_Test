# dict 의 검사 와 반복문 활용
dct1 = dict(name='김성민', age=24)
dct2 = {'name':'김우중', 'age':27}
print(type(dct1), dct1)
print(type(dct2), dct2)
print("dct1에 age 항목이 있는가?", 'age' in dct1)
print("dct1에 height 항목이 있는가?", 'height' in dct1)
if('height' in dct1) :          # 항목(키)의 존재유무 파악을 활용하는 방법
    print(dct1['height'])
else :
    dct1["height"] = 170
    print(dct1["height"])

for key1 in dct1.keys() :    # dct1에 해당 키가 있으면 반복실행
    print(key1, " : ", dct1[key1])

for val in dct1.values() :   # dct1에 다음 값이 있으면 반복실행 -> dict형.values()
    print(val)

for i in dct1.items() :      # dict에 해당 항목의 쌍이 있으면 반복실행 -> dict형.items()
    print(i)