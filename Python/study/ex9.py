var1 = 200
var2 = "김성민"
print(var2, "의 점수는 ", var1, "입니다.")
p1 = int(input("국어 점수 입력 : "))
p2 = int(input("영어 점수 입력 : "))
p3 = int(input("수학 점수 입력 : "))
tot = p1 + p2 + p3 #총점
print("총점 : ", tot)
print("평균 : ", format(tot/3,"3.3f"))