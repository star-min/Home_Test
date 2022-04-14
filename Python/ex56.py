from re import findall, sub
# findall() : 필요한 데이터만 패턴을 적용하여 가져올때
# sub() : 불필요한 데이터만 패턴을 적용하여 제외시킬 때
# compile() : 패턴을 만들때
# match() : 데이터가 특정 패턴과 일치할때

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
# 4차 : 영문 제거    첫글자만 추출할 경우 '^[가-힣]'
#data4 = [".".join(findall('[가-힣]+', text)) for text in data3]
#print(data4)
# 4차 : 한글 제거    첫글자만 추출할 경우 '^[가-힣]'
data4 = [" ".join(findall('[A-Z]+', text)) for text in data3]
print(data4)
