num = int(input("请输入第一个数字:"))
num1 = int(input("请输入第二个数字:"))
s = input("请输入运算符(+,-,*,/):")

match s:
    case "+":
        print(f"{num + num1}")
    case "-":
        print(f"{num - num1}")
    case "*":
        print(f"{num * num1}")
    case "/" if num1 != 0:
        print(f"{num / num1}")
    case _:
        print("该操作不支持!")