dict = {"陆一":100,"陆二":200,"陆三":300}

# 添加/修改
dict["陆四"] = 20000
print(dict)

# 查询
print(dict["陆一"])
print(dict.get("陆一"))

# 获取所有key
print(dict.keys())
# 获取所有values
print(dict.values())
# 获取所有的键值对 key:values
print(dict.items())

# 删除
score = dict.pop("陆一")
print(score)
print(dict)

del dict["陆二"]
print(dict)

# 遍历
for k in dict.keys():
    print(f"{k}:{dict[k]}")

for item in dict.items():
    print(f"{item[0]}:{item[1]}")

for k,v in dict.items():
    print(f"{k}:{v}")
