# 位置参数 *args ---> 元组
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data,1)

print(calc_data(1,2,3,4,5,6,7,8,9))

# 关键字参数 **kwargs ---> 字典
def calc_data(*args,**kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值:{min_data},最大值:{max_data},平均值:{avg_data}")

    return min_data, max_data,avg_data

print(calc_data(1,2,3,4,5,6,7,8,9,round=2,print=True))