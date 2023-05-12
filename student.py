class Student():
    def __init__(self,name,age,energy,knowledge):
        self.name = name
        self.age = age
        self.energy = energy
        self.knowledge = knowledge
        print("{0}이 생성되었습니다. 나이 : {1} 남은 힘 : {2}".format(self.name,self.age,self.energy))
    def run(self):
        if self.energy >= 50:
            self.energy -= 50
            print("{0}이 달립니다. 남은 힘 : {1}".format(self.name,self.energy))
        else:
            print("힘이 부족하여 달릴 수 없습니다.")
    def study(self):
        if self.energy >= 30:
            self.energy -= 30
            self.knowledge += 20
            print("{0}이 공부합니다. 남은 힘 : {1} 지식 : {2}".format(self.name,self.energy,self.knowledge))
        else:
            print("힘이 부족하여 공부할 수 없어요")
student1 = Student("김학생",22,100,0)
student1.study()
student1.study()
student1.study()
student1.study()

