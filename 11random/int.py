import random
num = random.randint(1,100)

while True:
    s = int(input("请输入数字:"))
    if s > num:
        print("您输入的数字太大了!")
    if s < num:
        print("您输入的数字太小了!")
    else:
        print("恭喜您,猜对了!")
        break
print("随机的数字为:",num)
