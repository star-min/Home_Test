# 질의 쿼리를 url에 직접 지정하는 방법
# urllib, bs4, selenium 패키지 설치
import time
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'http://www.google.com/search?q='
plusUrl = input('무엇을 검색 할까요? ')
url = baseUrl + quote_plus(plusUrl)
driver = webdriver.Chrome(r'D:\\ksm\\test1\\chromedriver.exe')
driver.get(url)
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
v = soup.select('.yuRUbf')
# print(v)

for i in v :
    print(i.select_one('.LC20lb.DKV0Md').text)      # 제목
    print(i.a.attrs['href'])                        # 링크 주소
    print('\n')
driver.close()

