# calculator() 만들기
# calculator 함수는 사칙연산 기능을 제공합니다.
#사용자로부터 연산자 번호와 두 정수를 입력받으면 결과값이 출력.

def calculator():
    op = input("연산자를 선택하세요 (+,-,*,/): ")
    if op not in ['+','-','*',"/"]:
        print("잘못된 연산자입니다.")
        return
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    else:
        result = num1 / num2

    print(f"{num1} {op} {num2} = {result}")