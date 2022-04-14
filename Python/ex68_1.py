# bs4,
import os
from bs4 import BeautifulSoup
file = open('html01.html','r',encoding='UTF-8')
source = file.read()
print(source)

html = BeautifulSoup(source, 'html.parser')
# 하이퍼링크요소 (a) 의 요소 수를 구하여 출력 find_all(), len()
s = html.find_all('a')
print('하이퍼링크요소(a) 의 요소 수 : ', len(s))

for i in s :
    print(i.string)

# 패턴을 활용하여 필터링하여 출력 - compile() : 패턴을 등록할 수 있는 함수
import re
print('패턴으로 활용한 개체 속성으로 찾기')
pat = re.compile('http://')
links = html.find_all(href=pat)
print(links)
for i in links :
    print(i.string)

