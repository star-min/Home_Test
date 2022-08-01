import os, pickle
import re
file2 = open('webdata1.pickle', mode='rb')
load_data = pickle.load(file2)
print(load_data)

# 전처리 작업(필터링)
def clean_text(text_string) :
    txt1 = re.sub("[,.?!:$\'\";]", '', text_string)
    txt1 = re.sub('[!@#$%^&*()]|[0-9]', '', txt1)
    txt1 = txt1.lower()
    txt1 = re.sub('[a-z]', '', txt1)
    txt1 = ' '.join(txt1.split())
    return txt1
clean_data = [clean_text(row) for row in load_data]
print(clean_data)


# 단어로 분리하기
w_cnt = {}
for text in clean_data :
    for word in text.split() :
        w_cnt[word] = w_cnt.get(word, 0) + 1

print(w_cnt['우크라이나'])

# 2건 이상 출현된 단어 정리
# del w_cnt['심상정']        # 불필요한 단어의 개수는 소거
new_w_cnt = {}
for word, cnt in w_cnt.items() :
    if cnt >= 2 and len(word) >= 2 and len(word) :
        print(word, '=>', w_cnt[word])
        new_w_cnt[word] = new_w_cnt.get(word, cnt)

# 차트나 그림으로 출력가능한 항목과 수치로 만듦
from collections import Counter
counter = Counter(new_w_cnt)
top_word = counter.most_common(5)       # 큰 거 5대 항목

import matplotlib.pyplot as plt
words = []      # 항목 리스트
counts = []     # 값 리스트
# dict를 list로 변경
for word, count in top_word :
    words.append(word)
    counts.append(count)
# print(words)
# print(counts)

# 한글이 적용이되는 폰트를 불러와야한다 아니면 깨짐
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

# 차트로 출력
plt.plot(words, counts)
plt.show()

