import os, pickle
import re

file = open('webdata1.pickle', mode='rb')
news_data = pickle.load(file)

# 전처리 작업
def clean_text(text_string) :
    txt1 = re.sub('[,.?!:\'\";]', '', text_string)
    txt1 = re.sub('[@#$^&()*]|[0-9]', '', txt1)
    txt1 = txt1.lower()
    txt1 = txt1.sub('[a-z]', '', txt1)
    txt1 = ''.join(find_all(txt1.split()))
    return txt1
# print(clean_text(news_data))          ! 함수는 출력할수없음
clean_data = [clean_text(row) for row in news_data]