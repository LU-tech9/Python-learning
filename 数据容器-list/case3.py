num = []
for i in range(1,21):
    num.append(i**2)
print("原始列表：",num)

num1 = []
for n in num:
    if n % 2 == 0:
      num1.append(n**2)
print("筛选后的列表：",num1)

num3 = [i**2 for i in range(1,21)]
print("原始列表:",num3)

num4 = [123,44,39,48,67,89,21,24]
new_list = [i**2 for i in num4 if i %2 ==0]
print("筛选后的列表:",new_list)