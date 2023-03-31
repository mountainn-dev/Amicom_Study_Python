words = ["bird","rat","eagle","cat"]
print(words)
oldWord = input("바꾸고자 하는 단어를 입력하세요 : ")
newWord = input("새로운 단어를 입력하세요 : ")
oIndex = words.index(oldWord) # 입력받은 oldWord를 찾고 그 위치를 저장.
words[oIndex] = newWord   #입력받은 newWord를 찾은 oldWord의 위치에 끼워넣기.
print(words)