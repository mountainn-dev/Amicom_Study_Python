pocket = 20000    # 수중 잔액
balance = 10000   # 계좌 잔액

def deposit(money):
    global pocket, balance
    pocket -= money
    balance += money

def withdraw(money):
    global pocket, balance
    balance -= money
    pocket += money

deposit(10000)
withdraw(5000)


def print_header(header):
 with open("test.txt", "a", encoding="utf-8") as t:
  for i in range(len(header)):
   if i != len(header)-1:
    print(header[i].ljust(8), end="", file=t)
  else:
    print(header[i].ljust(8).strip(), file=t)
def print_line(line):
 column_count = len(line)
 for i in range(column_count):
  print_product_info_with_format(line, i)
def print_product_info_with_format(line, i):
 with open("test.txt", "a", encoding="utf-8") as t:
  if i == 0:
   print(line[i].ljust(7), end="", file=t)
  elif i == 1:
   price = int(line[i].strip())
 print("{0:<8,}".format(price), end="", file=t)
   else:rate = float(line[i].strip())
  print("{0:<8.1%}".format(rate), file=t)
  price_file = open("C:/Users/HongSeongSan/Desktop/price.csv", "r", 
encoding="utf-8")
header = price_file.readline().split(",")
print_header(header) # 헤더 출력
while True: # 내용 출력
 line = price_file.readline().split(",")
 if line.__contains__(''): # 데이터에 null 값이 존재할 때 = 라인이
끝날 때
 break
else:
 print_line(line)