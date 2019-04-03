from module import *

print("$ python calculator.py")
print("  Menu")
print("--------")
print("1: add")
print("2: sub")
print("3: multiply")
print("4: divide")
print("5: stop")

while 1:
    print(":", end="")
    select = input()
    if(select == "1"):
        print("num1:", end="")
        former = int(input())
        print("num2:", end="")
        latter = int(input())
        a = cal(former, latter)
        print(cal.add(a))
    elif(select == "2"):
        print("num1:", end="")
        former = int(input())
        print("num2:", end="")
        latter = int(input())
        a = cal(former, latter)
        print(cal.sub(a))
    elif(select == "3"):
        print("num1:", end="")
        former = int(input())
        print("num2:", end="")
        latter = int(input())
        a = cal(former, latter)
        print(cal.mul(a))
    elif(select == "4"):
        print("num1:", end="")
        former = int(input())
        print("num2:", end="")
        latter = int(input())
        a = cal(former, latter)
        print(cal.div(a))
    elif(select == "5"):
        print("계산기 프로그램 종료")
        break
    else:
        print("숫자는 1~5 사이의 정수만 입력하세요")
        continue
