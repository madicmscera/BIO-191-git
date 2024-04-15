rows = 3
columns = 5

for i in range(0,rows):
    for j in range(0,columns):
        if j%2 == 0:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print ()

