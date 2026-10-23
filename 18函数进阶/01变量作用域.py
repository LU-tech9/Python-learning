# 全局变量:在函数外部或内部都可以使用的
num = 100


def circle_area(r):
    # 局部变量:只能在函数内部使用
    pi = 3.14
    area = pi * r * r

    global num
    num = 10000
    print("num=", num)

    return area


c_area = circle_area(10)
print(c_area)

print("num =", num)