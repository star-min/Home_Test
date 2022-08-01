import json
# JSON 파일의 입출력 처리
import os

with open(os.getcwd()+'/data/datafile.JSON', 'r') as f :
    json_data = json.load(f)
# print(json_data)
print(json.dumps(json_data))
print('k5의 가격', json_data['K5']['price'])