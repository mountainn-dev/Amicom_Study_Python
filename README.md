# Amicom 파이썬 스터디 연습장

- 아미콤 파이썬 스터디 전용 레포지토리입니다.
- 매 주차마다 학습 내용과 실습 내용을 README 파일과 각자의 .py 파일에 자유롭게 작성하시면 됩니다.
- 정해진 작성 형식은 없습니다.


## 1주차 배운 내용
- # 문제 1
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
이런걸 했다.

## 2주차 배운 내용

# 문제 1
words = ["bird", "rat", "eagle", "cat"]
print(words)
oldWord = input("입력 : ")
newWord = input("입력 : ")
oldWordindex = words.index(oldWord)
words[oldWordindex] = newWord
print(words)

# 문제 2
users = {}
userData = input("이름, 나이, 학년")
tmpData = userData.split(" ")
users[tmpData[0]] = [tmpData[1], tmpData[2]]

name = input("조회하고자 하는 사용자의 이름을 입력해주세요: ")
print("\n 이름:" + name + "나이: " + users[name][0] + "학년: " + users[name][1])


## 3주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 4주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 5주차 배운 내용
- 이곳에 작성하시면 됩니다.

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
