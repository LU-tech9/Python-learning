football_set = {"陆一","陆二","陆三","陆四"}
basketball_set = {"陆一","陆三"}
s1 = football_set.intersection(basketball_set)
print(s1)

s2 = football_set & basketball_set
print(s2)

s3 = football_set.difference(basketball_set)
print(s3)

s4 = football_set - basketball_set
print(s4)

s5 = {s for s in football_set if s not in basketball_set}
print(s5)

all_set = football_set.union(basketball_set)

all_set1 = football_set|basketball_set

all_list = [*football_set, *basketball_set]

for s in all_set:
    print(f"{s}选修了{all_list.count(s)}课程")