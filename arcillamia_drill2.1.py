age = int(input("What is your age? "))
license = input("Do you have a fishing license in MN (yes/no)? ")
parentlicense = input("Does your parent have a fishing license (yes/no)? ")

#Legal to fish in MN if age 15 and under but parent has license or age 16 and older but with own license

legal = ((age <= 15) and (parentlicense == "yes")) or ((age >= 16) and (license == "yes"))

if legal:
    print ("You are legal to fish in MN.") 
    
else:
    print ("You are not legal to fish in MN.")

