# 1. input() 함수를 사용하여 사용자로부터 사용자 정보(userData)를 입력받습니다.
# 2. 사용자 정보는 이름(name), 나이(age), 학년(grade) 로 3가지가 존재합니다.
# 3. 입력 완료 후 각 정보를 users 변수에 저장합니다.
# 4. input() 함수를 사용하여 사용자로부터 이름을 입력받으면, 해당 사용자의 정보가 출력됩니다.

users = {}
userData = input("사용자 정보를 입력해주세요(이름 나이 학년) : ")
key = userData.split(" ")
users["name"] = key[0]
users["age"] = key[1]
users["grade"] = key[2]
print(users)
name = input("조회하고자 하는 사용자 이름을 입력해주세요 : ")
print("이름 : " + name + " 나이 : " +str(users["age"]) + " 학년 : " + str(users["grade"]))


# users = {}
# userData = input("사용자 정보를 입력해주세요(이름 나이 학년) : ")
# key = userData.split(" ")
# users[key[0]] = [key[1],key[2]]
# print(users)
# name = input("조회하고자 하는 사용자 이름을 입력해주세요 : ")
# print("이름 : " + name + "\t나이 : " + users[name][0] + "\t학년 : " + users[name][1])