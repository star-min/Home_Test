import os
# mode : 파일을 열 때 어떠한 용도로 열지를 지정
# r : 읽을 목적, w : 오버라이트할 목적(덮어쓰기), a : 내용을 추가할 목적
# x : 오버라이트할 목적(파일이 없을 때)
print(os.getcwd())      #현재 디렉토리 위치
pat = os.getcwd()
try :
    f1 = open(pat+'test1.txt', 'r')
    print(f1.read())
except :
    print("해당 파일이 존재하지 않습니다.")