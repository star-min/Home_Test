# 대입 연산자
a = 100
b = 20
c = b = a
print(a, b, c)

a = a + 1
a += 1
print("a : ", a)

a = a - 1
a -= 1
print("a : ", a)
i = 20
j = 30
i, j = j, i
print("i=", i,"j=", j)

lst = [10, 30, 15, 20, 25]
print(lst)
v1, v2, v3, *v4 = lst # *은 리스트의 나머지 요소를 대입시킨다
print(v1, v2, v3, v4)
*v1, v2 = lst # 앞에있을경우
print(v1,v2)
v1, *v2, v3 = lst # 중간에 있을경우
print(v1,v2,v3)
