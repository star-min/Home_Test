# 팩토리얼을 계산하는 재귀함수의 빈 칸을 채우시오.

def Factorial(n):
    if n == 1 :
        return  1
    else :
        n += n-1
    return n
result_fact = Factorial(5)
print("팩토리얼 결과 : ", result_fact)