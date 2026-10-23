def reg_stu(name,age,gender,city="Shanghai"):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return name,age,gender,city

stu = reg_stu("张三",18,"male","Beijing")
print(stu)
stu = reg_stu("张三",18,"male")
print(stu)