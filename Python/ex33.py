# 알고리즘(algorithm) : 어떤 특정한 문제나 업무를 해결하기 위한 프로그램적 절차나 방법
# 최대값을 계산하는 알고리즘 : 각 값들을 비교하며 가장 큰 값을 찾아내는 절차나 방법
lst = [90, 75, 95, 80, 85, 70]
max = 0     # 최대값을 저장하기위한 변수로서 0으로 초기화해야 함
for i in lst :       # 반복비교를 위한 for문
    if i > max :
        max = i
print("최대값은 : ", max)

# 최소값 알고리즘
min = 100
for i in lst :
    if min > i :
        min = i
print("최소값은 : ", min)

# 선택 정렬(selection sort) : 순서가 정해질 값과 비교대상의 값을 선택하여 값들을 순서대로 재배치
for i in range(0, len(lst)-1, 1) :
    for j in range(i+1, len(lst), 1) :
        if lst[i] > lst[j] :
            lst[i], lst[j] = lst[j], lst[i]
print(lst)

# 이진 검색 : 이미 순서대로 오름차순 정렬이 되어 있는 자료형에서
# 중간 값을 이용하여 중간 값보다 찾는 값이 더 크면, 중간 값의 뒤에서 찾아 나가는
# 검색 방법

value = int(input("찾을 숫자를 입력해주세요"))     # 찾을 값 입력
low = 0                                        # 검색 시작 위치
high = len(lst) - 1                            # 검색 마지막 위치
loc = 0                                        # 찾은 위치
state = False                                  # 찾았는지 못 찾았는지 유무 판단자
while low <= high :                            # low(시작위치)와 high(마지막위치)가 서로 교차되면
    mid = ([low] + high) / 2)                  # 중간값의 위치
    if lst[mid] > value :                      # 찾는 값이 중간값보다 작으면
        high = mid - 1
    elif lst[mid] < value :                    # 찾는 값이 중간값보다 크면
        low = mid + 1
    else :                                     # 찾는 값이 중간값과 일치하면 찾은 것으로 간주
        loc = mid                              # 현재 중간값의 위치를 찾는 값의 위치로 대입
        state = True                           # 값의 위치를 찾았으므로 찾았다고 판단해줌
        break                                  # 값의 위치를 찾았으므로 반복 종료
if state :                                     # 값의 위치를 찾았으면 그 위치를 출력
    print("찾은 위치 : ", loc+1)
else :                                         # 값의 위치를 찾지 못함
    print("값을 못 찾음")
