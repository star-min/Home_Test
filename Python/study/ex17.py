# random 수 출력하기 위한 random 모듈 임포트
# import 란? : 파이썬의 내장모듈이 아닌 외장모듈을 불러오기
import random
#help(random) # 해당 모듈의 속성과 메서드를 보기
a = random.random()     # 0~1 숫자를 임의로 발생
b = random.randint(1, 10)
print(a, b)

blist = ["김성민", "김서은", "김우중", "박상용", "김기태"]
plist = [10000, 1000, 0, 5000, 100000000]
if '김성민' in blist :
    print("김성민 있음!")
else :
    print("김성민 없음!")
i = 0
while i < len(blist) :
    i+=1
    c = random.randint(0, 4)
    d = random.randint(0, 4)
    print(blist[c], " : ", plist[d])

