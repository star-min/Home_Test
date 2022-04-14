# format양식 문자
# format 함수
rad = 20                #반지름
pi = 3.141592           #원주율
l = rad * 2 * pi        #원의 둘래길이
a = rad * rad * pi      #원의 면적
print("반지름 : ", format(rad, "8d"))
print("원주율 : ", format(pi, "5.3f"))
print("원의 둘래 : ", format(l, "2.4f"))
print("원의 면적 : ", format(a, "10.2f"))
# f : 실수의 소수점 이하 자릿수    .3f
# d(decimal) : 정수 표시할 자릿수 , 10진수
# o(octo) : 8진수 ( 89 -> 3o -> 111(8진수 3자리))
print("8진수로 출력 : ", format(89, "3o"))
# x(hexa) : 16진수 정수 , 한자리를 16까지늘림
print("197을 16진수로 출력 : ", format(157, "5x"))
# s(string) : 문자열로 표시

# 형식 문자
var1 = "김성민"
var2 = 27
var3 = 100.1
print("이름 : %s, 나이 : %d, IQ : %.1f" %(var1, var2, var3))    #문자,정수,실수 각 형태에따라 순서를 맞춰야함, %는 접속사
print('이름 : %s, 나이 : %d, IQ : %.1f' %(var1, var2, var3))