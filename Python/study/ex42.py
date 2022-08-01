# 재귀 함수 : 내부에서 자기자신의 함수를 호출해서 처리하는 함수

def fnc1(a, b) :
    return a+b

def Count(n) :
    if n == 0 :
        return 0
    else :
        print(n-1)
        Count(n-1)      # 호출자의 parameter의 값 만큼 자기 자신의 함수를 호출

Count(4)