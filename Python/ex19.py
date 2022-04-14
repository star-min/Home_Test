# 반복문 : while 문, for 문
# while문 : 반복 횟수나 카운트 변수가 별도로 지정됨
# for문 : 반복횟수나 카운트변수가 내포가 됨
# for 변수 in 열거형객체 :
#   실행문
# 열거형 객체 : list , set, tuple, dict -> 다른 언어에서 는 배열 이라함
lst =["김성민", "김기태", "정몽주", "김두한"]   # 열거형 객체
print(lst)
for i in lst :
    print("회원명 : ", i)

# range(begin. end) 함수를 활용
for i in range(1, 20) :
    print(i)

for i in range(15) :    # end 값만 적용됨
    print(i)

for i in range(1, 20, 3) :  # 세 번째 인수는 step
    print(i)

# 더미 데이터를 만드는 법
import random
lst1 = []
for i in range(10) :    # 0~9
    r = random.randint(2, 20)
    lst1.append(r)
    print(i)
print("lst1 : ", lst1)