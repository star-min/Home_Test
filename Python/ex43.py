# Factorial(누승) : 6! = 6*5*4*3*2*1
# 재귀함수 : 함수의 반복처리를 요구하는 수열에서 자주 사용
def Fact(n) :
    if n == 1 :
        return 1
    else :
        result = n * Fact(n-1)      # 1씩 감소 시켜 곱하기
        return result

print(Fact(10))