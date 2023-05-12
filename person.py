# 1. Person 은 이름(name) 과 나이(age), 힘(energy) 로 이루어져있습니다.
# 2. Person 이 달리기를 할 경우(run), 힘이 감소합니다.
# 3. Person 은 힘이 부족할 때는 달릴 수 없습니다. 

class Person():
    def __init__(self,name,age,energy):
        self.name = name
        self.age = age
        self.energy = energy
        print("{0}이 생성되었습니다. 나이 : {1} 남은 힘 : {2}".format(self.name,self.age,self.energy))
    def run(self):
        if self.energy >= 50:
            self.energy -= 50
            print("{0}이 달립니다. 남은 힘 : {1}".format(self.name,self.energy))
        else:
            print("힘이 부족하여 달릴 수 없습니다.")


person1 = Person("홍길동",20,100)
person1.run()
person1.run()
person1.run()
