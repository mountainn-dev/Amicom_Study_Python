'''from random import *

print(random())
# 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)
# 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))
# 0 ~ 10 미만의 값 생성'''

#문제 1번
from random import *
'''print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)
print(int(random() * 29) + 1)'''
# 문제 1
from random import *
number = (int)(random() * 29) + 1
print("%d 개" %number)

# 문제 2
print("A\nBC\nDEF")

#문제 3
name = "김진재"
from random import *
age = (int)(random() * 30) + 1
print("안녕하세요 제 이름은 {name}이며, 제 나이는 {age}살입니다.".format(name = "김진재", age = (int)(random() * 30) + 1 ))
# 해설
age = randint(10, 30)
name = "Kelbin"
print("안녕하세요 제 이름은 %c%s 입니다. 제 나이는 %d입니다." %(name[0].upper(), name[1:], age))

