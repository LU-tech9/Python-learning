

menu = """
#######教务管理系统#######
#     1.添加学生信息     #
#     2.修改学生信息     #
#     3.删除学生信息     #
#     4.查询学生信息     #
#     5.列出所有学生     #
#     6.统计班级成绩     #
#     7.退出系统        #
#######################

"""
print(menu)

student_information = {}

choice = int(input("请输入选择(1-7):"))
while True:
    print(menu)
    choice = input("请输入选择(1-7):")
    match choice:
        case "1":
            name = input("请输入学生姓名:")
            chinese = float(input("请输入语文成绩:"))
            math = float(input("请输入数学成绩:"))
            english = float(input("请输入英语成绩:"))

            if name in student_information:
                print("该学生信息已存在~")
            else:
                student_information[name] = {"语文成绩":chinese,"数学成绩":math,"英语成绩":english}
        case "2":
            name = input("请输入要修改的学生姓名:")
            chinese = float(input("请输入修改的语文成绩:"))
            math = float(input("请输入修改的数学成绩:"))
            english = float(input("请输入修改的英语成绩:"))

            if name in student_information:
                student_information[name] = {"语文成绩":chinese,"数学成绩":math,"英语成绩":english}
            else:
                print("该学生不存在~")
        case "3":
            name = input("请输入要删除的学生姓名:")

            if name not in student_information:
                print("该学生不存在~")
            else:
                del student_information[name]
        case "4":
            name = input("请输入要查询的学生姓名:")

            if name not in student_information:
                print("该学生不存在~")
            else:
                print(student_information[name])
        case "5":
            print(student_information.keys())
        case "6":
            if not student_information:
                print("系统中暂无学生信息,请先添加学生~")
                continue

            chinese_scores = []
            math_scores = []
            english_scores = []


            for student_name, scores in student_information.items():
                chinese_scores.append(scores["语文成绩"])
                math_scores.append(scores["数学成绩"])
                english_scores.append(scores["英语成绩"])


            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(chinese_scores) / len(chinese_scores)

            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(math_scores) / len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(english_scores) / len(english_scores)


            chinese_max_students = [name for name, scores in student_information.items() if scores['chinese'] == chinese_max]
            chinese_min_students = [name for name, scores in student_information.items() if scores['chinese'] == chinese_min]

            math_max_students = [name for name, scores in student_information.items() if scores['math'] == math_max]
            math_min_students = [name for name, scores in student_information.items() if scores['math'] == math_min]

            english_max_students = [name for name, scores in student_information.items() if scores['english'] == english_max]
            english_min_students = [name for name, scores in student_information.items() if scores['english'] == english_min]


            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"     最高分学生: {chinese_max_students}")
            print(f"     最低分学生: {chinese_min_students}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"     最高分学生: {math_max_students}")
            print(f"     最低分学生: {math_min_students}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"     最高分学生: {english_max_students}")
            print(f"     最低分学生: {english_min_students}")
            print("========================")

        case "7":
            break
        case _:
            print("非法输入!")
