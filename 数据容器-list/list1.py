s = [1 , 2 , "A" , True]
print(type(s))

s[1] = 100
print(s)

del s[0]
print(s)

for item in s:
    print(item)