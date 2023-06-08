today = int(input("오늘 일자를 입력하세요: "))
if today % 4 == 0:
    print("오늘은 장날입니다.")
else:
    print("오늘은 장날이 아닙니다.")

users = {}
i = 0
while i < 3:
    userData = input("사용자 정보를 입력해주세요(이름 나이 학년) : ")
    tmpData = userData.split(" ")
    users[tmpData[0]] = [tmpData[1], tmpData[2]]
    i += 1

    print(users)


def calculator():
 print("계산기를 작동합니다.\n")
 operatorNum = int(input("원하는 연산 번호를 입력해주세요.(1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈): "))
 num1 = int(input("첫 번째 수를 입력해주세요: "))
 num2 = int(input("두 번째 수를 입력해주세요: "))
 if operatorNum == 1:
  print("\n 결과값: {0}".format(num1 + num2))
 elif operatorNum == 2:
  print("\n 결과값: {0}".format(num1 - num2))
 elif operatorNum == 3:
  print("\n 결과값: {0}".format(num1 * num2))
 else:
  print("\n 결과값: {0}".format(num1 / num2))
calculator()




star = "*"
whiteSpace = " "
for i in range(5):
 print(abs(i - 5) * whiteSpace + (((i * 2) + 1) * star) + (abs(i - 5) * 
whiteSpace))
