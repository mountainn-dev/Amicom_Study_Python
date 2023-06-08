# 2주차 과제 2번 문제의 코드를 활용하여, 총 3번의 user 정보를 입력받습니다.
# for문과 while문을 번갈아 사용하여 구현해봅니다.
users = {}
for i in range(1,4):
    userData = input("사용자 정보를 입력해주세요(이름 나이 학년) : ")
    key = userData.split(" ")
    users[key[0]] = [key[1],key[2]] # 입력받은 값(이름 나이 학년)중 이름을 딕셔너리의 Key에 저장, 나이와 학년을 Value에 저장
print(users)