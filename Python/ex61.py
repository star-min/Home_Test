import os
print("현재 파일 경로 : ", os.getcwd())
print("현재 디렉토리 안의 목록 : ", os.listdir())
realPath = "data/test4.txt"
print("디렉토리의 상대 경로 표시 : ", realPath)
print("디렉토리의 절대 경로 표시 : ", os.path.abspath(realPath))
# 절대경로 : 파일의 위치를 처음 위치부터 해당 파일 까지의 경로
# 상대경로 : 현재 디렉토리를 기준으로 해당 파일까지의 경로
aPath = 'D:\\ksm\\test1\\data\\test4.txt'
bPath = 'D:\\ksm\\test1\\data\\'
print("현재 파일의 디렉토리 표시 : ", os.path.dirname(aPath))
print('디렉토리의 존재유무 : ', os.path.exists(bPath))
print('파일의 존재유무 : ', os.path.isfile(aPath))
print("디렉토리 존재 유무 : ", os.path.isdir(bPath))
print('디렉토리와 파일을 분리 : ', os.path.split(aPath))
print("파일 사이즈 : ", os.path.getsize(aPath))
