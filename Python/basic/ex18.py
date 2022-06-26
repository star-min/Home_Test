# random 모듈을 활용하여 주사위를 두개 던졌을 때 두 개의 주사위 결과를 출력
import random
ju1 = random.randint(1, 6)
ju2 = random.randint(1, 6)
julist = [ju1, ju2]
print("두개의 주사위값 결과 : ", julist)

#무작위로 1~45 까지 번호를 여섯개 출력하는 프로그램
mujak = 0
while mujak < 6:
    mujak += 1
    print("로또번호 :", random.randint(1, 45))

while True :
    a = int(input("수를 입력"))
    b = random.randint(1, 10)
    if a == b :
        print("성공 :", a)
        break