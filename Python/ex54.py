# ex54.py - sub의 반대인 split, compile 활용하기
# 필요한 데이터만 추출
from re import split, compile, match
mtext = """ http://www.google.com
http://www.naver.com
http://www.daum.net
"""
# 1차 필터링 - 데이터를 특정 구분자로 분리하기
lst1 = split("\n", mtext)       # re모듈을 임포트 해서 사용
print(lst1)
lst2 = mtext.split("\n")        # 기본 내장 str의 모듈
print(lst2)
# 2차 필터링 - null 데이터는 제외하고, 특정 패턴이 있는 데이터 추출
pat = compile("http://")        # compile ("패턴") 패턴을 생성
lst3 = [site for site in lst1 if match(pat, site)]
print(lst3)
