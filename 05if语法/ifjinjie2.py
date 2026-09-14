num = int(input("请输入数字:"))
if num>0:
    print(f"{num}为正数")
elif  num < 0:
    print(f"{num}为负数")
else:
    print(f"{num}为0")

name = int(input("请输入用户名:"))
password = int(input("请输入密码:"))
if name == 666 and password == 666:
    print("登陆成功")
elif name == 777 and password == 777:
    print("登录成功")
else:
    print("用户名或密码错误")

money = int(input("请输入商品原价总金额:"))
if money >= 500:
    print("应付金额为:",money*0.8)
elif money >= 300 and money < 500:
    print("应付金额为:",money*0.9)
elif money <=100:
    print("应付金额为:",money)
