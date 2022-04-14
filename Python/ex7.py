#논리 연산자 :여러 비교 연산자를 이어붙여 조건을 판단할 때 사용
var1 = 60
var2 = 50
var3 = 40
var4 = 70
print("var1 >= var2 and var3 >= var4 : ", (var1 >= var2 and var3 >= var4)) #and 둘다 참
print("var1 >= var2 or var3 >= var4 : ", (var1 >= var2 or var3 >=var4))  #or 어느하나라도 참이면 참
print("not var1 >= var2 : ", not (var1 >= var2))