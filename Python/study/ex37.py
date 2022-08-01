# builtins 모듈 : 내장 모듈
su1 = 27
su2 = -27
su3 = 23.82
su4 = 23.28
print("su2의 절대값 : ", abs(su2))

lst = [40, "김성민", True, 89.27]
print("모든요소가 값이 있는가? : ", all(lst))     # all(열거형) : 모든 요소가 값이 있거나 참이면 참
print("어떤 하나라도 값이 있는 요소가 있는가? : ", any(lst))     # any(열거형) : 요소 중에서 하나라도 값이 있거나 참이면 참
print("숫자 40을 2진수로 : ", bin(40))
print("숫자 40을 8진수로 ", oct(40))
print("숫자 40을 16진수로 : ", hex(40))
print("도움말 출력 : ")
help(len)
print("목록 출력 : ")
dir(len)            # 클래스, 함수, 변수 목록 표시
enumerate(lst)      # 열거형 자료의 키와 값을 모두 출력
print("3의 5승 : ", pow(3, 5))
print("su3을 반올림하여 출력 : ", round(su3))
