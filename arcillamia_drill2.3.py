int1 = int(input("Please enter an integer: "))
int2 = int(input("Please enter another integer: "))
int3 = int(input("Please enter a third integer: "))

integers = [num for num in [int1, int2, int3] if num %2 !=0]

if integers:
    print(max(integers), "is the greatest")

else:
    print("None of the integers are odd")