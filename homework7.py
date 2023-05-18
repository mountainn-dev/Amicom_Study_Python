'''try:
    value = int(input("정수를 입력하세요: "))
    print("Process finished with exit code 0")
except ValueError as e:
    input_value = input("잘못된 값을 입력하셨습니다. 입력값: {input_value}")
    print("Process finished with exit code 0")
'''

class NumberRangeError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"NumberRangeError: 입력된 값({self.value})이 허용된 범위(1~10)를 벗어났습니다. 해당 값이 0으로 대체됩니다. "


def validatevalue(v):
    try:
        number = int(v)
        if number < 1 or number > 10:
            raise NumberRangeError(number)
        return number
    except ValueError:
        return 0
    except NumberRangeError as e:
        print(e)
        return 0


value = input("입력: ")
number = validatevalue(value)
print(number)
print("Process finished with exit code 0")