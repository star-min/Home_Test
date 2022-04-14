# list의 크기를 키보드로 입력 받은 후, 입력 받은 크기만큼 임의 숫자를 list에 추가하고, list의 크기를 출력하시오.
# 출력결과 예시
# vector 수 : 3
# 4
# 2
# 5
# vector 크기 : 3
vector = int(input("vector 수 : "))
list = []
for i in range(vector) :
    list.append(input())
    i += 1
print(len(list))



# lsit 크기를 키보드로 입력 받은 후, 입력 받은 크기만큼 임의 숫자를 list에 추가한다. 이후 list에서 찾을 값을
# 키보드로 입력한 후 해당 값이 list에 있으면 "yes", 없으면 "no"를 출력하시오.
# 출력결과 예시
# vector 수 : 5
# 1
# 2
# 3
# 4
# 5
# 3
# yes

if input("list에 있을것같은 값 입력 : ") in list :
    print("YES")
else :
    print("NO")