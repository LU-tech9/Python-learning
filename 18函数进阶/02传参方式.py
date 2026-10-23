def reg_stu(name,age,gender,city):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return name,age,gender,city

#位置参数
stu = reg_stu("张三",18,"male","Beijing")
print(stu)

#关键字参数
stu = reg_stu("name = 张三",age = 18,gender = "male",city = "Beijing")
print(stu)

#位置参数 + 关键字参数(位置参数必须在关键字参数之前)
stu = reg_stu("张三",18,gender = "male",city = "Beijing")
print(stu)
