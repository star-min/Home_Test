# 이진파일 : 2진수로 된 파일 어떠한 형태로든 가공이나 처리가 가능
# 파이썬의 이진 파일은 pickle 형로 저장함
import pickle
data = '나는 너를 아직 사랑하지 않아'
try :
    test4 = open('data/test4.txt', 'r')
    data = test4.read()
except :
    print("오류")
finally:
    test4.close()
pickle1 = open('data/pickle1.pickle', 'wb')
pickle.dump(data, pickle1)
pickle1.close()

pickle2 = open('data/pickle1.pickle', 'rb')
data2 = pickle.load(pickle2)
print(data2)
print("데이터 길이 : ", len(data2))