s =[1,2,3,4,5,6,7,8,9,10]
# 最后添加
s.append(10000000000)
print(s)
# 在指定前插入
s.insert(1,100)
print(s)
# 移除匹配值
s.remove(10)
print(s)
# 删除指定位置 若没有默认最后一个
s.pop(0)
print(s)
# 排序
s.sort()
print(s)
# 反转顺序
s.reverse()
print(s)
