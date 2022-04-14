# 사용자 정의 클래스 만들기 : 클래스(붕어빵틀), 객체(붕어빵)

class Calulator :
    def __init__(self):
        self.result = 0
        self.data = 1

    def add(self, num):         # parameter(o), return(o)
        self.result+=num
        return self.result

    def multi(self, num):
        self.data*=num
        return self.data

cal1 = Calulator()              # cal1은 Calulator 클래스로 부터 만들어진 객체
cal2 = Calulator()

print(cal1.add(50))
print(cal1.add(100))

print(cal2.add(200))
print(cal2.add(80))

cal2.multi(10)
cal2.multi(8)
print(cal2.multi(5))

# 클래스 생성방법
# calss  클래스명 :
#       필드 : 클래스 안에 있는 필요 변수
#       [필드1]
#       ....
#       def __init__(self) :
#           [필드의 초기화]
#       def 메서드명(self[, 매개변수, ...])
#           메서드 실행문
#   특정 클래스로부터 객체 생성
#       객체명 = 클래스명()

# 함수 문법 : 매개변수(인수)나 반환값이 있고 없고에 따라 종류가 나뉨
# def 함수명([매개변수1, 매개변수2, ....]) :
#       [사용자 정의 실행문]
#       [return 반환값]

# 함수는 정의부와 호출부가 있으며,
# 함수는 정의되어 있는 대로 호출해야 실행됨