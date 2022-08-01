# 정규표현식 모듈(re) 활용
from re import findall
# finball은 필요한 데이터나 패턴만 찾아서 변환 -> 필요한 데이터 추출
# 주요 메타문자
# .a(a로 끝나는 것), a.(a로 시작하는 것), ^a(a로 시작하는 것), a$(a로 끝나는 것
# a*(a가 0번 이상 반복되는 것), a+(a가 1번 이상 반복되는 것), a?(a가 없거나 1번 있는 것)
# abc|ABC(abc이거나 ABC인 경우), a(a만 선택), [a-z](a부터 z까지 선택)
#[^a](a가 아닌 것만 선택)
# {2,}(2글자 이상), {,3}(3글자 미만), {3,6}(3글자 이상 부터 6글자 미만)
str1 = "hello javascript 14 I like c, python, java just like it 1004 사랑해요~"
print("python의 존재 유무 : ",findall("python", str1))
print("숫자면 추출 : ", findall("[0-9]", str1))
print("4자리 숫자만 추출 : ", findall("[0-9]{4}", str1))
print("10진수 숫자 3자리 이상 추출 : ", findall("\\d{3,}", str1))
print('한글 데이터만 추출 : ', findall('[가-힣]{2,}', str1))
print("영어 3글자 이상 추출 : ", findall('[a-z|A-Z]{3,}', str1))
print('ke로 시작하는 데이터 추출 : ', findall('ke...', str1))
print('ke로 끝나는 데이터 추출 : ', findall('...ke', str1)) # .찍은 수만큼 범위 늘어남