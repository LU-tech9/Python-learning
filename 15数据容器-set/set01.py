S1 = {1,2,2,3,4,5,5,6,7}
print(S1)

# 定义空集合
s2 = set()

# 添加元素
S1.add(10000000)
print(S1)

# 删除指定元素
S1.remove(10000000)
print(S1)

# 随机删除一个元素并返回
e = S1.pop()
print(e)
print(S1)

# 清空集合
S1.clear()
print(S1)

m = {1,2,3,4,5,6,7}
n = {1,2,9,100,123}

# 求差集 存在第一个集合,但不存在第二个集合
print(m.difference(n))
print(n.difference(m))

# 求并集
print(m.union(n))
print(n.union(m))

# 求交集
print(m.intersection(n))
print(n.intersection(m))

