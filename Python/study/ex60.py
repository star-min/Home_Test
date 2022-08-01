import os
data = '안녕하세요 김성민 입니다. \nhello my name is SeongMin Kim'
try :
    file1 = open('data/test4.txt', 'w')
    file1.write(data)
except Exception as e:
    print('파일에 대한 처리가 이루어 지지 못했습니다.' +e)
finally :
    file1.close()

# 디렉토리 = 폴더
print(os.listdir())     # os.listdir() : 현재 디렉토리 안의 파일 목록
# os.rename("123.txt", 'test1.txt')   # os.rename() : 파일 이름 변경
# os.remove('test1.txt')    # 파일 삭제
# os.mkdir('data2')     # 디렉토리 생성
# os.rmdir('data2')     # 디렉토리 삭제
# print(os.getcwd())      # 현재 디렉토리 경로 표시
os.chdir('data')
# print(os.getcwd())
print(os.getcwd())
try :
    f2 = open('test4.txt', 'r')      # 위에서 test4를 ansi로 인코딩되게 만들어서 utf로 읽으면 오류
    print(f2.read())
 except :
    print("x")
finally:
    f2.close()
perent = str(os.pardir())       # pardir() : 상위 디렉토리 경로
os.chdir('d:\\kim4\\test1')
print(os.getcwd())