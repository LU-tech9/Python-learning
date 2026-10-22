def triangle_area(d, g):
    area = d * g / 2
    return area


s = triangle_area(10, 20)
print(s)


def count_aeiou(s):
    num = 0
    for i in s:
        if i in "aeiouAEIOU":
            num += 1
    return num


print(count_aeiou("Hello World"))


def calc_score(score_list):
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s


s_list = [666, 666, 750, 666, 590]
max_score, min_score, avg_score = calc_score(s_list)
print("最高分:", max_score)
print("最低分:", min_score)
print("平均分:", avg_score)
