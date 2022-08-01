# 몬테카를로 시뮬레이션 : 현실 상 모의실험을 하기가 힘근 경우 프로그램으로 대신하여 모의실험을 할 수 있도록 한것
# 테스트 케이스를 제작
import random


def coin(n) :           # n은 동전을 던지는 횟수
    result = []
    for i in range(n) :     # result = [0, 1, 1, 0, ...]
        r = random.randint(0,1)
        if r==1 :
            result.append(1)

        else :
            result.append(0)
    return result
print(coin(10))

def monte(n) :
    cnt = 0
    for i in range(n) :
        cnt += coin(1) [0]
        res = cnt / n
    return res
print("동전을 100번 던졌을 때 앞면이 나올 확률 : ", monte(10000))