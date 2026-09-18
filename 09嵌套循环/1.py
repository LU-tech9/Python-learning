c = int(input("请输入长度:"))
k=int(input("请输入宽度:"))

for s in range(k):
    for b in range(c):
        print("*",end="  ")
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()
