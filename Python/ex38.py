# 피타고라스 정리 : 빗변의 제곱 = 높이의 제곱 + 밑변의 제곱
# 높이의 제곱 = 빗변의 제곱 - 밑변의 제곱
# 밑변의 제곱 = 빗변의 제곱 - 높이의 제곱
# 빗변의 제곱 구하기
import math
def pythago0(h, l) :
    s = h**2 + l**2
    return math.sqrt(s)
print("높이 : 10, 밑변이 : 6 일 때 빗변의 길이 : ", pythago0(10,6))
print(math.sqrt(4))

def pythago1(h, l) :
    s = h**2 + l**2
    return s**(1/2)
print("높이 : 10, 밑변이 : 6 일 때 빗변의 길이 : ", pythago1(10,6))

def pythago2(s, h) :        #밑변의 길이 구하기
    l = s**2 - h**2
    return l**(1/2)
print("사선 : 10, 높이 : 5, 밑변 : ", pythago2(10, 5))

def pythago3(s, l) :        #높이의 값을 구하기
    h = s**2 - l**2
    return h**(1/2)
print("사선 : 10, 밑변 : 8, 높이 : ", pythago3(10, 8))