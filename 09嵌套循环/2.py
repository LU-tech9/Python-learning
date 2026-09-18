num = int(input("请输入数字:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
    print()