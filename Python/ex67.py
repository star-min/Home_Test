# 특정단어를 입력 받아 그 단어를 구글에 검색하여 검색된 결과에서 제목과
# url을 출력
# selenium, bs4, urllib, selenium-browser, selenium-Chrome, selenium-driver-updater, Chromedriver 설치
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 쿼리 스트림
# baseurl = 'https://www.google.com/search?q='
plusurl = input('검색어를 입력해주세요 : ')
# url = baseurl + urllib.parse.quote_plus(plusurl)
# print(url)
drm = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(drm)
url = 'https://www.google.com'
driver.get(url)
time.sleep(1)
element = driver.find_element_by_name('q')
element.send_keys(plusurl)
element.submit()
# html = driver.page_source
# print(html)
# soup = BeautifulSoup(html)
