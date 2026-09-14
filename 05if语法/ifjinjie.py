year = int(input("请输入年份:"))
if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year}是润年")
else:print(f"{year}是平年")

num = int(input("请输入数字:"))
if num%2==0:
    print("此数字为偶数")
else:print("此数字为奇数")

old = int(input("请输入年龄:"))
if old>=18:
    print("您已成年")
else:print("您未成年")