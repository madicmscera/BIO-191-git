integer = int(input("Enter integer to generate filled and hollow square: "))

for i in range(integer):
    filled = integer * "*"
    if i == 0  or i == integer-1:
        hollow = "*" * integer
    else:
        hollow = "*" + " " * (integer-2) + "*"

    print(filled, hollow)