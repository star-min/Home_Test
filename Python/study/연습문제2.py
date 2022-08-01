# 1~100 사이에서 3의 배수이면서 2의 배수가 아닌 수를 한 줄에 출력하고, 누적합을 출력 하시오.
Hap = 0
for i in range(1, 101) :
    if i % 3 == 0 and i % 2 != 0 :
        print(i, end = ' ') # end = ' 띄고 ' 라고해야함 붙이면안댐
        Hap += i
print( Hap) #/n 적용법


# 다음과 같은 multiline의 문자열 객체를 이용하여 단어를 추출하고 단어의 개수를 출력하시오.
# multiline="""안녕하세요. 파이썬 세계로 오신걸
# 환영합니다.
# 파이썬은 비단뱀 처럼 매력적인 언어입니다."""
multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
lst = []
wd = []
su = 0
for i in multiline.split(sep = "\n") :
    lst.append(i)
    for w in i.split(sep = "") :
        wd.append(w)
        print(w)
        su += 1
print(su)
print(lst)
print(wd)
