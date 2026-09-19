while True:
    s = input("请输入用户名:")
    b = input("请输入密码:")
    if s ==" " or b==" ":
        print("用户名或密码不能为空!")

    if s == "666" and b == "666":
        print("登陆成功!")
        break
    elif s == "777" and b == "777":
        print("登陆成功!")
        break
    else:
        print("登录失败,用户名或密码错误")
