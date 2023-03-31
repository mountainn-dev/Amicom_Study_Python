
'''# 문제 1
words = ["bird", "rat", "eagle", "cat"]
print(words)
oldWord = input("입력 : ")
newWord = input("입력 : ")
oldWordindex = words.index(oldWord)
words[oldWordindex] = newWord
print(words)'''

# 문제 2
users = {}
userData = input("이름, 나이, 학년")
tmpData = userData.split(" ")
users[tmpData[0]] = [tmpData[1], tmpData[2]]

name = input("조회하고자 하는 사용자의 이름을 입력해주세요: ")
print("\n 이름:" + name + "나이: " + users[name][0] + "학년: " + users[name][1])
