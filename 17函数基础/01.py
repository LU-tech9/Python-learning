def out_line():
    print("______________________")

out_line()


# 函数的参数与返回值
def circle_area(r):
    area = 3.14 * r ** 2
    return area


s = circle_area(10)
print(s)


def rectangle_area(l, w):
    area = l * w
    return area


print(rectangle_area(10, 20))


# round(target,保留几位小数 填写数字)
def circle_area_len(r):
    """
    根据圆的半径计算圆的面积和周长
    :param r:半径
    :return:圆的面积，圆的周长

    """
    return 3.14 * r * r, round(2 * 3.14 * r, 1)


al = circle_area_len(10)
print(al)


# 函数的嵌套调用
# 栈结构 先进后出
def function_a():
    print("a...before")
    function_b()
    print("a...after")


def function_b():
    print("b...before")
    function_c()
    print("b...after")


def function_c():
    print("c...")


function_a()

print("函数调用完毕~")