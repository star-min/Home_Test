import os
import urllib.request as req
from bs4 import BeautifulSoup
url = 'http://media.daum.net'
res = req.urlopen(url)      # beckground 방식
source = res.read()         # 요청 URL에 담긴 정보를 불러옴
source = source.decode('UTF-8')
html = BeautifulSoup(source, 'html.parser')
aTages = html.select('a[class=link_txt]')
# print(aTages)

# 필터링
cr_data = []
cnt = 0
for atag in aTages :
    ++cnt
    atagStr = str(atag.string)
    if(atag.string!=None) :
        cr_data.append(atagStr.strip())
# print(len(cr_data))

import pickle
file = open('webdata1.pickle', mode='wb')
pickle.dump(cr_data, file)


# file2 = open('webdata1.pickle', mode='rb')
# load_data = pickle.load(file2)
# print(load_data)