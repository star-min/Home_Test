# builtins 내장 모듈
lst = [90, 40, 60, 70, 50, 45, 65] # 열거형
print(lst)
# emumerrate는 열거형 자료를 인덱스와 값으로 나누어 줌
# for 인덱스변수, 콘텐츠변수, in enumerate(열거형변수명) :
for i, c in enumerate(lst) :
    print("인덱스 : ", i, "값 : ", c)
dict1 = {"name":"김성민","age":26, "height":175}
for i, c in enumerate(dict1) :
    print("인덱스 : ", i, "키 : ", c, ":", dict1[c])