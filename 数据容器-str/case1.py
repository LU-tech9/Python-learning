s = ".  Hello-Python-Hello-World.  "

#find()查找字符串第一次出现的索引位置
s1 = s.find("-")
print(s1)

#count()统计出现次数
s2 = s.count("o")
print(s2)

#upper()转为大写
s3 = s.upper()
print(s3)

#lower()转为小写
s4 = s.lower()
print(s4)

#split()按照字符串将制定字符串切割
s5 = s.split("-")
print(s5)

#strip()去除字符串两端空格
s6 = s.strip()
print(s6)

#replace替换
s7 = s.replace("-","_")
print(s7)

#startswith/endswith判断字符串是否以指定字符串开头/结尾并返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Hello"))
