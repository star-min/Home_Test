# 자연어 처리 : 특정 문장이나 데이터 열에서 불필요한 특수문자, 숫자 디타 제거하는 방법
from re import findall, sub
textData = [' korean# Fighting 1234 ', '우리 $%나라 ^대한 민국 4567', '^_^ #@@김성민 잘생김 87645']
# 1차 : 영문 소문자를 대문자로 변경 - 스크래핑을 위한 데이터 가공
data1 = [t1.upper() for t1 in textData]
print(data1)
# 2차 : 특수문자 제거
data2 = [sub('[\^_!@#$%]+', '', text) for text in data1]
print(data2)
# 3차 : 숫자 제거
data3 = [sub('[1-9]','', text) for text in data2]
print(data3)
# 4차 : 한글 제거
data4 = [sub('[\가-힣]+', '', text) for text in data3]
print(data4)
# 5차 : 영어 제거
data5 = [sub('[A-Z]+', '', text) for text in data4]        #[a-z|A-Z]
print(data5)
# 6차 : 공백 제거                                # 책에 안나옴
data6 = [text.strip() for text in data5]
print(data6)
# 7차 null값 제거                               # 책에 안나옴
from re import compile, sub, match
data7 = [text for text in data6 if text]        # 리스트만 가능한 방법
print(data7)
