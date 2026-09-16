day = int(input("请输入星期几(1-7):"))
match day:
    case 1:
        print("周一:早八")
    case 2:
        print("周二:早八")
    case 3:
        print("周三:早八")
    case 4:
        print("周四:早八")
    case 5:
        print("周五:早八")
    case 6|7:
        print("周末")
    case _:
        print("输入错误!")