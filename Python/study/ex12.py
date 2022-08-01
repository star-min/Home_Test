#문자열 저장 및 출력
singleLine = "오늘은 불금인데 뭐하나"
multiLine = """오늘 저랑 
불금을 함께하실분을
모십니다."""
print(singleLine)
print(multiLine)

data = "i love thejoeun academy"
print(data[0])
print(data[7])
print(data[2:5])        #begin:end = begin 부터 end 전까지 -> slicing
print(data[:6])         #begin 생략시 처음부터
print(data[7:])         #end 생략시 begin 부터 끝까지
print(data[1:6:9])      # begin:end:step  1부터 6까지 9칸씩 이동하면서
print(data[-3:])        # -는 오른쪽부터
print(data[:-3])
print(data[-6:-1])
print(data[-1:-6])
print(data[::2])        # 문자를 2개씩 건너띄면서   , begin 과 end 를 생략할시 전체
print(data[0]*10)       # *특정문자 반복 출력