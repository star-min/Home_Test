data= """나는 자랑스런 대한민국의 아들로
이름은 김성민이라고 하며,
전주김씨 48대손이며, 나이는
27세로 백성들의
별 이라는 이름을
가지고 있다.
"""
lst = [] # 줄
wd = []  # 단어
for i in data.split(sep = "\n") :
    lst.append(i)
    for w in i.split(sep = " ") :
        wd.append(w)
print(lst)
print(wd)
# 웹 크롤링 하여 필터링 전에 하는 작업
#기초통계, 응용통계