num1 = [12,46,58,90,80,48,99,78]
num2 = [23,49,80,90,999,789,998]

# for num in num1:
#     num2.append(num)
# print("合并后的原始列表:",num2)
#
# num3 = []
# for num in num2:
#     if num not in num3:
#         num3.append(num)
# print("筛选后的列表:",num3)

# 解包 + *
# num = [*num1,*num2]
# print(num)

num = num1 + num2
print(num)