out_line = lambda : print("---------------")
out_line()

def add(x,y):
    return x + y

add = lambda x,y : x + y
print(add(100,200))


data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript"]
print(data_list)

data_list.sort(key=lambda item : len(item))
print(data_list)