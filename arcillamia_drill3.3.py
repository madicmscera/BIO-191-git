def prime(number):
    if number < 2:
        return False
    for i in range(2, int(number//2) + 1):
        if number % i == 0:
            return False
    return True

def print_primes(given_integer):
    count = 0
    number = 2
    while count < given_integer:
        if prime(number):
            print(number, end=" ")
            count += 1
        number += 1

given_integer = int(input("Please enter an integer: "))
print("The first", given_integer, "prime numbers are:")
print_primes(given_integer)

print()