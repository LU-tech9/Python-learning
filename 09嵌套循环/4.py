for i in range(1,9):
    for j in range(1,9):
        if (j+i)%2==0:
            print("+",end=" ")
        else:
            print("-",end=" ")
    print()
