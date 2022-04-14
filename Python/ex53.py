from re import sub
# 불핑필요한 재료 추출
data = "우리 * 나라 1234 korea~! ^ 5678 화이팅 $ fighting"
print(data)
# 1차 필터링
text1 = sub('[\*~!^$]+', '', data)
print(text1)
# 2차 필텨링
text2 = sub('[1-8]+','',text1)
print(text2)
# 스크래핑을 위한 텍스트를 리스트로 변환하기
lst = text2.split()
print(lst)
lst2 = list(text2)   # 그냥 사용하면 전부 띄어짐
print(lst2)
str1 = "김성민/심인보/이동은/김서은"
print(str1.split("/"))