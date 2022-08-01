#변수명은 알파벳으로 시작하고, 대소문자를  구분하며, 예약어를 사용할수 없다
#예약어(Reeserved Word) = keyword : print(x) print1(0)
# printNumber(0) : 카멜 방식 ,단어를 읽기쉽도록 두번째단어부터 첫글자를 대문자호
#print_number(0) : 언더스코어 방식, 단어 중간마다 언더스코어(_)
#변수명은 누구든지 그 기능이나 저장된 데이터를 쉽게알수 있도록하는것이 관례
#식별자(Identifiers) : 변수, 클래스, 모듈, 함수
import keyword
print(keyword.kwlist)
