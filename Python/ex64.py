import os
import pandas as pd
doc = pd.read_excel(os.getcwd()+'/data/exce0.xlsx')
# print(doc)
doc2 = pd.read_excel(os.getcwd()+'/data/excel1.xlsx', sheet_name=2)
# print(doc2)
doc3 = pd.read_excel(os.getcwd()+'/data/excel1.xlsx', header=None)    # 엑셀의 맨 윗줄이 종목이 아니라 데이터일경우 이걸로 없애줌
# print(doc3)
doc4 = pd.read_excel(os.getcwd()+'/data/excel1.xlsx', names=['번호', '이름', '등급'])
# print(doc4)
doc5 = pd.read_excel(os.getcwd()+'/data/excel1.xlsx', usecols=[1, 2])
# print(doc5)
doc6 = pd.read_excel(os.getcwd()+'/data/titanic.xlsx', nrows=6, skiprows=2)
# print(doc6)
import csv
f = open(os.getcwd()+'/data/excel1.csv', 'r')
# print(f.read())
data = csv.reader(f)
# print(data)
for line in data :
    print(line)
f.close()
