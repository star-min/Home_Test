# 가변인수가 적용되는 함수
# 가변인수란? : parameter(인수)의 개수가 변화될 수 있는 인수

def fnc1(name, *names) :        # name : 단일기억장소변수, *names : tuple
    print(name)                 # **names : dict
    print(names)
fnc1("김서은", "김성민", "김우중", "김기태", "성윤식", "오민우", "이강석")