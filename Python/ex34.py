# 프로그램 모듈과 패키지, 함수, 클래스

# def = define(정의하다 선언하다)
def fnc1() :    # fnc1은 함수명     - parameter(x)(매개변수), return(x)
    print("Hi~! Python~!")
fnc1()          # 모든 함수는 실행을 하려면 호출을 해야함

def fnc2() :    # parameter(x), return(o)
    return input("나이입력 : ")   # 호출시 숫자를 반환
age = fnc2()
print(age)

def fnc3(a, b) :    # parameter(o), return(x)
    print("곱한 결과 : ", a*b)
fnc3(10, 5)

def fnc4(a, b) :    # parameter(o), return(o)
    return a*b
multi = fnc4(6, 8)
print("매개변수로 값을 대입하여 곱한 결과를 반환반음 : ",multi)