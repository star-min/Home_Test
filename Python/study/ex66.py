# 크롤링 : 시스템에 접근하여 필요한 데이터를 가져오는 것
# 스크래핑 : 필터링을 거쳐 필요한 데이터로 가공하거나 추출
# 파싱 : 스크랩을 하거나 저장하려고 할 경우 디지털 데이터로 전환하여
# 웹 데이터 수집 및 처리 과정 : 크롤링 -> 파싱 및 필터링 -> 스크래핑 -> 기업이나 수급처에 필요한 자원으로 제공
# 크롤링 도구 : urllib
# 파싱 도구 : BeautifulSoup(4)
# 스크래핑 도구 : matplotlib
import os
import urllib.request as ur
from bs4 import BeautifulSoup
url = "http://www.naver.com/index.html"
res = ur.urlopen(url)           # 특정 URL에 있는 문서를 저장
# print(res)
data = res.read()               # 소스코드 읽기
# print(data)
src = data.decode("UTF-8")      # 한글 디코딩
print(src)
# 검색된 내용을 모두 res1.txt 로 저장

try :
    res1 = open('res1.txt', 'w', encoding='UTF-8')
    res1.write(src)
except :
    print("크롤링된 정보를 담지 못했습니다.")
finally:
    res1.close()

try :
    res2 = open('res2.html', 'w', encoding='UTF-8')
    res2.write(src)
except :
    print("x")
finally:
    res2.close()

# 파싱하고 res2.txt 로 저장
html = BeautifulSoup(src, 'html.parser')
# print(html)

a1 = html.find('img')
print(a1)

a2 = html.find_all('a')
res = []
# a2의 텍스트만 필터링 하여 res4.txt에 저장
file4 = open("res4.txt", "w", encoding="UTF-8")
for i in a2 :
    if(i.string!=None):
        print(i.string)
        file4.write(i.string)
        file4.write("\n")
file4.close()

# try:
#     res3 = open('res2.txt', 'w', encoding='UTF-8')
#     res3.write(html)
# except :
#     print("x")
# finally:
#     res3.close()

