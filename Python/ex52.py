from re import match
jumin = '950522-1234567'
email = 'zxzx00262@gmail.com'
res1 = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
res2 = match('[a-z0-9]+@[a-z]', email)
if res1 :
    print("주민번호 형식이 맞습니까?", res1)
else :
    print("주민번호 형식이 아닙니다.")
if res2 :
    print("이메일 형식이 맞습니다.")
else :
    print("이메일 형식이 아닙니다.")