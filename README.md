# Amicom 파이썬 스터디 연습장

- 아미콤 파이썬 스터디 전용 레포지토리입니다.
- 매 주차마다 학습 내용과 실습 내용을 README 파일과 각자의 .py 파일에 자유롭게 작성하시면 됩니다.
- 정해진 작성 형식은 없습니다.


## 1주차 배운 내용
- Github Setting, 스터디 진행 방향 및 계획

## 2주차 배운 내용
- 2023.03.30.THU
    <파이썬 리스트와 반복문>
    리스트 선언, 연산자, 리스트에 요소 추가하기(append, insert, extend), 리스트에 요소 제거하기(del, pop(), remove, clear)


    (1)
    numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

    for number in numbers:
        if number >= 100:
            print("100 이상의 수: ", number)


    (2)
    numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

    for number in numbers:
        if number % 2 == 1:
            print(number, "는 홀수입니다.")
        else:
            print(number, "는 짝수입니다.")
    

    (3)
    numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

    for number in numbers:
        print(number, "는", len(str(number)), "자릿수입니다.")
    

    (4)
    list_of_list = [
        [1, 2, 3],
        [4, 5, 6, 7],
        [8, 9],
    ]

    for line in list_of_list:
        for item in line:
            print(item)
    

    (5)
    numberes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    output = [[], [], []]

    for number in numbers:
        output[(number + 2)% 3].append(number)
    
    print(output)
1


## 3주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 4주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 5주차 배운 내용
- * 팀원 중간고사 미완료로 활동하지 못했음 *

## 6주차 배운 내용
- 2023.05.04 Thu

    (1) 딕셔너리
        dict = {
            "A": 65,
            "a": 97
        }
        print(dict["A"])    // Result: 65

        if "B" in dict:
            print(dict["B"])
        else:
            print("없는 키입니다.")
        
        * if dict.get("B") == None: *

        # dict의 값 : {}
        # dict의 결과 : {"name":"구름"}
        # dict에 적용할 코드: dict["name"] = "구름"
        

## 7주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 8주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 9주차 배운 내용
- 이곳에 작성하시면 됩니다.

## 10주차 배운 내용
- 이곳에 작성하시면 됩니다.
