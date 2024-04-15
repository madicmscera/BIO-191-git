N = int(input("Input: "))
print (N)
cnt = 1
while cnt <= N:
    for j in range(0, cnt):
        print("*", end="")
        if (j != cnt):
            print(" ", end="")
    cnt = cnt + 1
    print()