# 중첩 예외처리
name = "LeeWanYong"
try :               #정상(시도)구문 구절
    # div = 100 / 0
    # f = open("c:\\kkt.txt")
    if name == "LeeWanYong" :
        raise ValueError
except ZeroDivisionError as e:          # except 중 하나만 실행이 됨
    print("0으로 나누려고 시도하였음. 오류 정보 : ", e)
except FileNotFoundError as e:
    print("없는 파일을 열려고 시도하였음. 오류 정보 : ", e)
except Exception as e:
    print("원인 불명의 에러가 존재합니다.")
except ValueError as e:
    print("회원가입이 거절된 사용자 입니다.")
finally :       # 이걸 안쓸경우 파일을 닫지않고 시스템을 종료하는것 반드시 finally를 사용 미사용시 다시열때 오류
    print("try 구절이 성공적으로 실행 했든 실패했든지 관계없이 무조건 실행되어야 문장")

# 파이썬의 예외의 종류
# SyntaxError : 잘못된 문법
# NameError : 선언되지 않은 변수나 함수, 클래스를 사용할 때
# ZeroDivisionError : 0 으로 나누려고 할 때
# IndexError : 열거형에서 없는 인덱스를 요청할 때
# KeyError : 열거형 중 에서 dict 일 경우 해당 키가 없는데 요청하는 경우
# AttributeError : 클래스에서 선언되지 못한 필드(속성)을 활용할 때
# FileNotFoundError : 없는 파일이나 파일 경로가 잘못 되었을 때
# TypeError : 처리되지 못하는 데이터 타입일 때
# ValueError : 잘못된 값이 들어가 있는 경우
