age = int(input("Please enter your age: "))
naturalborn = input("Are you a natural born citizen of the U.S. (yes/no)? ")
resident = int(input("How many years have you resided in the U.S.? ")) 

eligible = ((age >= 35) and (naturalborn == "yes") and (resident >= 14))

if eligible:
    print("You can run for president of USA.")
else:
    print("You are not eligible to run for president of USA.")
