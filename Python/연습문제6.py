# 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오
# 1 : [10, 1, 5, 2, 10, 1, 5, 2]            lst 원소를 2배 생성하여 result 변수에 저장 및 출력하기
# 2 : [10, 1, 5, 2, 10, 1, 5, 2, 20]        lst의 첫 번째 원소에 2를 곱하여 result 변수에 추가 및 출력하기
# 3 : [1, 2, 1, 2]                          result의 홀수 번째 원소만 result2 변수에 추가 및 출력하기

lst = [10, 1, 5, 2]
result = lst * 2
print(result)

result.append(result[0]*2)
print(result)

result2 = []
i = 0
for j in result :
    if i % 2 != 0 :
        result2.append(j)
    i += 1
print(result2)