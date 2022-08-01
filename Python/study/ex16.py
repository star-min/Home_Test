# 반복문 while
i = tot = 0     # 두 변수 초기화
# while문은 조건이 만족하는 동안 실행
# while 조건:
#   반복실행문장
while i < 1000 :
    i += 1        # i 가 1씩 증가
    tot += i      # tot에 i를 누적
print("1부터 1000까지의 합계", tot)

#1부터 100까지의 짝수의 합계

dlist = []
i = tot = 0
while i < 100 :
    i += 5
    dlist.append(i)
print("5의 배수들 : ",dlist)
print("5의 배수의 개수 ",len(dlist))

klist = []
i = tot = 0
while i < 100 :
    i += 1
    if i % 5 == 0 :
        klist.append(i)
print(klist)

tlist = []
i = tot = 0
while True :    #무한루프
    i += 1
    if i >= 100 :
        break
    if i % 5 == 0 :
        tlist.append(i)
print(tlist)