# height 변수에 별의 층수를 입력하면 각 층마다 별의 개수가 한 개씩 증가하여 출력되고,
# 마지막줄에 별의 개수가 출력되도록 함수의 빈 칸을 채우시오

def StarCount (height) :
    height = int(input('height : '))
    star = 0
    for i in range(1, height + 1):
        for j in range(i):
            print("*", end="")
            star += 1
        print("")
    return star
print('start 개수 : %d' %StarCount(height))






# 테스트용 코드
star = 0
height = int(input('height : '))
    for i in range(1, height+1) :
        for j in range(i) :
            print("*", end="")
            star += 1
        print("")
print(star)