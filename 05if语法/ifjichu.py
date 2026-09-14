score = 750
if score==750:
    print("恭喜你,被录取了")
    print("欢迎进入大学生活")
print("----------------------------")

ok_account = 123456789
ok_password = 123456789
account = int(input("请输入账号:"))
password= int(input("请输入密码:"))
if account==ok_account and password==ok_password:
    print("登陆成功!")
if account!=ok_account or password !=ok_password:
    print("登录失败!账号或密码错误")

