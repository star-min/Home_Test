# 람다식 : 여러 명령과 실행문을 줄인 표현식 -> 함수를 더 줄인 표현식

def fnc1(a, b) :
    return a+b
print("a와 b의 더한결과 : ", fnc1(50, 17))

print("a + b = ", (lambda a, b: a+b)(50, 17))