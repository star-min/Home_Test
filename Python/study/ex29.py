# set의 사용법 : 중복성을 해결할 때
# 도메인 : 하나의 데이터 그룹에서 중복되지 않은 항목이 가져야할 값들
# 특정 항목이 가져야 할 값들 -> 성별 : 남, 여
domain = ["서울", "대전", "대구", "부산", "서울", "광주", "대전", "부산"]
print(domain)
city = set(domain)    # 중복성을 해결하려면 특정 자료형에서 set으로 변환
print(city)

data = """김성민 심인보 이동주 김기태
정몽주 이순신 광개토대왕 심인보 이동주 정몽주 이순신
김기태 심인보 이재명 윤석열 김기태 이재명
윤석열 심인보 이재명 이순신 정몽주 김성민"""
lst1 = data.split(sep='\n')
lst2 = []
print(lst1)
for i in range(0, len(lst1)) :
    lst2.append(lst1[i].split(sep= " "))
print(lst2)
