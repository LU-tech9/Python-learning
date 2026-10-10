dict = {"陆一":100,"陆二":200,"陆三":300}
print(dict)

# key必须是不可变类型(str int float tuple) 不能是list set dict

print(dict["陆一"])
dict["陆一"] = 333300000
print(dict)