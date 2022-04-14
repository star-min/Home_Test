# 클래스
class Member :      # 부모 (super) 클래스
    # 멤버변수
    name = None
    age = 0
    point = 0
    def __init__(self, name, age, point):       # 초기화 구문 = 생성자
        self.name = name            # self.멤버변수 = 매개변수
        self.age = age
        self.point = point
    def display(self):                          # 멤버 메소드
        print("이름은 ", self.name, "이며, 나이는 ", self.age, "입니다.")
    def __del__(self):                          # 소멸자
        del self.name
        del self.age
        del self.point
        print("객체가 '소멸' 되었습니다.")

mem1 = Member("김성민", 26, 100)
mem2 = Member("김서은", 26, 90)
mem2.name = "이순신"
mem1.display()
mem2.display()
print(id(mem1))
print(id(mem2))
del mem1

class User(Member) :    # 자식 (sub) 클래스
    gender = None
    def __init__(self, name, age, point, gender):
        self.name = name
        self.age = age
        self.point = point
        self.gender = gender
    def display(self):      # 메서드의 확장
        print("이름은 ", self.name, "이며, 나이는 ", self.age, "성별은 ",self.gender, "입니다.")
    def __del__(self):      # 소멸자의 확장
        del self.name
        del self.age
        del self.point
        del self.gender

# 오버라이딩(override) : 자식 클래스가 상속받은 자원들을 재정의(확장) 하는 것