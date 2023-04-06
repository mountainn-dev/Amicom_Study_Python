# Amicom 파이썬 스터디 연습장

- 아미콤 파이썬 스터디 전용 레포지토리입니다.
- 매 주차마다 학습 내용과 실습 내용을 README 파일과 각자의 .py 파일에 자유롭게 작성하시면 됩니다.
- 정해진 작성 형식은 없습니다.


## 1주차 배운 내용
```Python
from random import random
number = (int)(random() * 29) + 1
print("%d" %number)

print('  A\n BC\nDEF')

age= random. randint(10,30)
name='kelvin'
name= name.capitalize()
print('안녕하세요 제 이름은 {name}  이고 제 나이는 {age} 입니다')

from random import random
age = (int)(random() * 20) + 10
name = "kelvin"
print("안녕하세요 제 이름은 %c%s입니다. 제 나이는 %d 살 입니다."%(name[0].upper(), name[1:], age))
```

## 2주차 배운 내용
```Python
words=['bird','rat','eagle','cat']
print(words)
oldword = input('rat')
newword = input('dog')
oldwordIndex = words.index(oldword)
words[oldwordIndex] = newword
print(words)

userData= input('홍길동,19,3')
userData = userData.split()
users={'name': userDataList[0], 'age': int(userDatalList[1]), 'grade': int(userDataList[2])}
name=input(홍길동)
if name == users['name']:
    print(users)
    else
    print('일치하는 사용자 정보가 없습니다.')
    
users = {}
userData = input("사용자 정보를 입력해주세요(이름 나이 학년): ")
tmpData = userData.split(" ")
users[tmpData[0]] = [tmpData[1], tmpData[2]]

name = input("조회하고자 하는 사용자 이름을 입력해주세요: ")
print("\n이름: " + name + " 나이: " + users[name][0] + " 학년: " + users[name][1])
  



    
```    
    

## 3주차 배운 내용
- 이곳에 작성하시면 됩니다.
```Python
today= int(input('오늘의 날짜를 입력하세요:'))
if today % 4==0: 
   print('오늘은 장날입니다.')
else:
    print('오늘은 장날이 아닙니다.')

users = []
for i in range(3):
    user = {}
    user["name"] = input("이름을 입력하세요: ")
    user["age"] = int(input("나이를 입력하세요: "))
    users.append(user)

print(users)

# while 문 사용
users = []
i = 0
while i < 3:
    user = {}
    user["name"] = input("이름을 입력하세요: ")
    user["age"] = int(input("나이를 입력하세요: "))
    users.append(user)
    i += 1

print(users)

## 4주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 5주차 배운 내용
- 이곳에 작성하시면 됩니다

## 6주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 7주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 8주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 9주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 10주차 배운 내용
- 이곳에 작성하시면 됩니다.
