s = []
for i in range(10):
    num = int(input("请输入一个有效数字:"))
    s.append(num)
print(s)
s.sort()
print(f"排序后的列表为:{s}")
print(f"列表中最大值为:{s[-1]}",f"列表中最小值为:{s[0]}",f"列表中平均值为{sum(s)/len(s)}")



