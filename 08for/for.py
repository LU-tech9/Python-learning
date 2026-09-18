msg = input("请输入需要遍历的字符串:")
for s in msg:
     print(f"元素为:{s}")
else:
    print("程序结束")
total = 0
s = range(1,101)
for b in s:
    if b % 2 != 0:
        total += b

print("1-100所有奇数之和为:",total)