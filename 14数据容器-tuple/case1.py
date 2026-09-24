student =(
    ("s001","陆一",85,92,78),
    ("s002","陆二",92,88,95),
    ("s003","陆三",88,99,70),
    ("s004","陆四",90,97,79),
)
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
for i in student:
    total = i[2]+i[3]+i[4]
    avg = total/3
    print(f"{i[0]} {i[1]} {i[2]} \t{i[3]} \t{i[4]}\t{total} \t{avg:.1f}")

chinese_score=[i[2] for i in student]
math_score=[i[3] for i in student]
english_score=[i[4] for i in student]
print("语文成绩为：",chinese_score)
print("数学成绩为:",math_score)
print("英语成绩为:",english_score)

print(f"语文最低分为：{min(chinese_score)},最高分为：{max(chinese_score)},平均分为:{sum(chinese_score)/len(chinese_score)}")

print(f"数学最低分为：{min(math_score)},最高分为：{max(math_score)},平均分为:{sum(math_score)/len(math_score)}")

print(f"英语最低分为：{min(english_score)},最高分为：{max(english_score)},平均分为:{sum(english_score)/len(english_score)}")

print("优秀学生为:")
for i in student:
    total = i[2]+i[3]+i[4]
    avg = total/3
    if avg > 90:
        print(f"学生姓名：{i[1]} 平均分： {avg:.1f}")