# 제어문 : 조건문, 반복문, 기타 제어문
# 제어문 블록은 해당 명령의 첫 줄에 : 포함되고, 탭으로 해당 문장들을 블록처리함
# 조건문 : 주어진 조건에 따라 실행을 달리 하는 문장 -> if
# 반복문 : 실행 내용을 반복해야할 필요성이 있을 경우 사용하는 문장 -> while, for
# 기타 제어문 : continue, break
# 조건문
data = int(input("점수 입력"))
if data >= 80 :     #단순if
    print("합격")

if data >= 80 :
    print("합격")
else :
    print("합격이아님")

if data>= 90 :
    print("수")
elif data >= 80 : #90점 미만 내포
    print("우")
elif data >= 70 :
    print("미")
elif data >= 60 :
    print("양")
else :
    print("가")

jum1 = int(input("국어 점수를 입력하세요"))
jum2 = int(input("영어 점수를 입력하세요"))
jum3 = int(input("수학 점수를 입력하세요"))
#복수 조건에서 and : 주어진 조건에서 모두
# 국어, 영어, 수학 세 점수 모두 70점 이상이면 "합격" 아니면, "과락"
if jum1 and jum2 and jum3 >= 70 :
    print("합격")

else :
    print("과락")
#복수 조건에서 or : 주어진 조건에서 하나라도
# 국어, 영어, 수학 세 점수중에서 한과목 이라도 90점 이상이면 "과목우수", 아니면, "해당없음" 출력
if jum1 >= 90 or jum2 >= 90 or jum3 >= 90 :
    print("과목우수")
else :
    print("해당없음")

# 삼항조건 if
# 변수: 참 if (조건식) else 거짓
# num에는 jum1이 크면 jum1이 입력, jum2가 크면, jum2가 입력됨 -> 그러므로 더 큰 수만 입력됨
num = jum1 if(jum1 > jum2) else jum2
print("점수가 더 큰 과목 점수 : ", num)
