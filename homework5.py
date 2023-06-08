class Person:
    def __init__(self, name, age, energy):
        self.name = name
        self.age = age
        self.energy = energy

    def run(self):
        if self.energy >= 10:
            print(self.name + "이(가) 달립니다!")
            self.energy -= 10
        else:
            print("힘이 부족하여 달릴 수 없습니다.")

    def show_info(self):
        print("이름:", self.name)
        print("나이:", self.age)
        print("현재 에너지:", self.energy)


person = Person("홍길동", 25, 50)
person.show_info()
person.run()
person.run()
person.run()
person.show_info()
person.run()
person.run()
person.run()
person.show_info()


class Student:
    def __init__(self, name, age, energy, knowledge):
        self.name = name
        self.age = age
        self.energy = energy
        self.knowledge = knowledge

    def run(self):
        if self.energy >= 10:
            print(self.name + "이(가) 달립니다!")
            self.energy -= 10
        else:
            print("힘이 부족하여 달릴 수 없습니다.")

    def study(self):
        if self.energy >= 5:
            print(self.name + "이(가) 공부합니다!")
            self.energy -= 5
            self.knowledge += 10
        else:
            print("힘이 부족하여 공부할 수 없습니다.")

    def show_info(self):
        print("이름:", self.name)
        print("나이:", self.age)
        print("현재 에너지:", self.energy)
        print("지식:", self.knowledge)


student = Student("김철수", 20, 50, 30)
student.show_info()
student.run()
student.study()
student.run()
student.study()
student.study()
student.show_info()
