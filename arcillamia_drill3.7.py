integer = int(input("Enter integer to generate a diamond: "))

for i in range(1, integer + 1):
    print(" " * (integer - i), "*" * (2 * i - 1))

for i in range(integer - 1, 0, -1):
    print(" " * (integer - i), "*" * (2 * i - 1))

