# 리스트에 값을 반복문을 활용하여 대입할 수 있다. => 내포
a = [2, 4, 5, 3, 1]
b = a * 2
print("요소의 수가 두 배 확장", b)
c = [i * 2 for i in a]      # 요소의 값이 두배로
print("요소의 값이 두 배로 : ", c)

l = []
for k in a :
    l.append(k*2)
print("요소의 값이 두 배로 : ", l)

even = [i for i in range(0, 11) if i % 2 == 0]
print("0~10 에서의 짝수 리스트 : ", even)